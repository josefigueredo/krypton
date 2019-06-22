
--------------------------------------------------------------------------------

-- As sysoper

create user test_crypto identified by test_crypto;

grant connect to test_crypto;
grant create session to test_crypto;
grant create table to test_crypto;
grant create procedure to test_crypto;
grant create sequence to test_crypto;
grant create view to test_crypto;

alter user test_crypto quota 500M on users;

--------------------------------------------------------------------------------

-- As sysdba:

grant execute on dbms_crypto to test_crypto;


--------------------------------------------------------------------------------

-- As crypto

DROP TABLE ALGPARAMETERS;

CREATE TABLE ALGPARAMETERS
(
  ID  NUMERIC(15)        NOT NULL PRIMARY KEY,
  KEY VARCHAR2(100 BYTE) NOT NULL,
  IV  NVARCHAR2(100)     NOT NULL
);


CREATE OR REPLACE FUNCTION F_ENCRYPT (p_input VARCHAR2)
  RETURN VARCHAR2
AS
  v_encrypted_raw     RAW (2000);
  v_key               RAW (320);
  v_encryption_type   PLS_INTEGER := DBMS_CRYPTO.DES3_CBC_PKCS5;
  v_iv                RAW (320);
BEGIN
  SELECT key
       , iv
    INTO v_key
       , v_iv
    FROM algparameters
   WHERE id = 1;

  v_encrypted_raw := DBMS_CRYPTO.encrypt (
    src   => UTL_I18N.STRING_TO_RAW (p_input, 'UTF8'),
    typ   => v_encryption_type,
    key   => v_key,
    iv    => v_iv);
  RETURN UTL_RAW.CAST_TO_VARCHAR2 (UTL_ENCODE.base64_encode (v_encrypted_raw));
END;


CREATE OR REPLACE FUNCTION F_DECRYPT (p_input VARCHAR2)
   RETURN VARCHAR2
AS
   v_decrypted_raw     RAW (2000);
   v_key               RAW (320);
   v_encryption_type   PLS_INTEGER := DBMS_CRYPTO.DES3_CBC_PKCS5;
   v_iv                RAW (320);
BEGIN
   SELECT key
       , iv
    INTO v_key
       , v_iv
    FROM algparameters
   WHERE id = 1;

   v_decrypted_raw :=
      DBMS_CRYPTO.DECRYPT (
         src   => UTL_ENCODE.base64_decode (UTL_RAW.CAST_TO_RAW (p_input)),
         typ   => v_encryption_type,
         key   => v_key,
         iv    => v_iv);
   RETURN UTL_I18N.RAW_TO_CHAR (v_decrypted_raw, 'UTF8');
END;


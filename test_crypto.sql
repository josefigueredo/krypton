
--------------------------------------------------------------------------------

INSERT INTO ALGPARAMETERS VALUES (
  1,
  RAWTOHEX ('52AB32;^$!ER94988OPS3W21'),
  RAWTOHEX ('TY54ABCX')
);

COMMIT;


SELECT '20000000001'                       INPUT
     , F_ENCRYPT('20000000001')            ENCRYPTED_RESULT
     , F_DECRYPT(F_ENCRYPT('20000000001')) DECRYPT_RESULT 
  FROM DUAL;

--------------------------------------------------------------------------------

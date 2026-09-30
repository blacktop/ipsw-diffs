## libiodbcinst.2.dylib

> `/usr/lib/libiodbcinst.2.dylib`

```diff

 42.6.0.0.0
-  __TEXT.__text: 0xa2dc
+  __TEXT.__text: 0xa1a0
   __TEXT.__auth_stubs: 0x2b0
   __TEXT.__cstring: 0x5f9
   __TEXT.__const: 0x88

   __DATA.__common: 0x64
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /usr/lib/libSystem.B.dylib
-  UUID: 5EC275D8-2061-3DB8-8C2C-C940CF765412
+  UUID: 34FDBA1B-EDAD-345E-8757-E2DCE07556F1
   Functions: 112
   Symbols:   165
   CStrings:  88
Functions:
~ _SQLConfigDataSource_Internal : 4968 -> 4924
~ _SQLConfigDriver_Internal : 3216 -> 2972
~ _SQLGetInstalledDrivers_Internal : 916 -> 908
~ _SQLInstallDriverExW : 684 -> 680
~ _SQLInstallTranslatorExW : 684 -> 680
~ _GetTranslator : 1516 -> 1496
~ _SQLGetTranslator : 124 -> 128
~ __iodbcadm_getinifile : 596 -> 624
~ __iodbcdm_getdsnfile : 424 -> 428
~ _ValidDSN : 96 -> 100
~ _ValidDSNW : 88 -> 92
~ _dm_SQL_W2A : 132 -> 140
~ _dm_StrCopyOut2_A2W : 188 -> 196
~ _dm_StrCopyOut2_W2A : 188 -> 196
~ _dm_SQL_U8toW : 448 -> 444
~ _utf8towcs : 188 -> 184
~ __iodbcdm_cfg_init : 188 -> 200
~ __iodbcdm_cfg_refresh : 1040 -> 1048
~ __iodbcdm_cfg_nextentry : 196 -> 204
~ __iodbcdm_cfg_write : 1092 -> 1024
~ _install_from_ini : 1244 -> 1240
~ _rtrim : 160 -> 152
~ _GetPrivateProfileString : 476 -> 480
~ _SQLGetPrivateProfileStringW : 748 -> 744

```

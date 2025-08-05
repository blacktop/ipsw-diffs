## IOGameControllerFamily_development

> `/System/Library/Extensions/IOGameControllerFamily.kext/IOGameControllerFamily_development`

```diff

-13.0.36.0.0
+13.0.39.0.0
   __TEXT.__const: 0x470
   __TEXT.__cstring: 0x21c6
-  __TEXT.__os_log: 0x8455
-  __TEXT_EXEC.__text: 0x2bc74
+  __TEXT.__os_log: 0x845c
+  __TEXT_EXEC.__text: 0x2bc7c
   __TEXT_EXEC.__auth_stubs: 0x520
   __DATA.__data: 0xc8
   __DATA.__common: 0x268

   __DATA_CONST.__mod_term_func: 0x50
   __DATA_CONST.__const: 0x5558
   __DATA_CONST.__kalloc_type: 0x800
-  UUID: 00CD702E-8812-397E-B2D9-B60EB25DBF08
+  UUID: DDC23DE7-C953-3876-9A31-63E4A17E6EA0
   Functions: 889
   Symbols:   1993
   CStrings:  577
Functions:
~ _OUTLINED_FUNCTION_20 : 12 -> 24
~ _OUTLINED_FUNCTION_23 : 24 -> 28
~ _OUTLINED_FUNCTION_24 : 28 -> 24
~ _OUTLINED_FUNCTION_27 -> _OUTLINED_FUNCTION_28 : 24 -> 12
~ __ZN16PSVR2SenseDevice26handleInputDataForTimesyncEPK19PSVR2SenseInputDataR18InputReportContext : 2564 -> 2572
CStrings:
+ "[%#010llx] #TRANSPORT Time synchronization state changed: %d -> %d (%llu)"
- "[%#010llx] #TRANSPORT Time synchronization state changed: %d -> %d"

```

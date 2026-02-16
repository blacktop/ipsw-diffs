## libAppleTCONUpdater.dylib

> `/usr/lib/updaters/libAppleTCONUpdater.dylib`

```diff

-201.80.2.0.0
-  __TEXT.__text: 0x5118
+201.100.3.0.0
+  __TEXT.__text: 0x5170
   __TEXT.__auth_stubs: 0x3d0
   __TEXT.__cstring: 0x1aec
   __TEXT.__const: 0x350
   __TEXT.__gcc_except_tab: 0x78
-  __TEXT.__unwind_info: 0x198
+  __TEXT.__unwind_info: 0x1a0
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x180
   __AUTH_CONST.__auth_got: 0x1f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: A614A228-F344-3E71-A99A-45F1ACF8AF89
-  Functions: 108
-  Symbols:   357
+  UUID: 3A6B3E0E-3579-3A2F-997E-3A12A84E55BA
+  Functions: 109
+  Symbols:   359
   CStrings:  304
 
Symbols:
+ __ZN25AppleTCONUpdateController5startEPK14__CFDictionaryPP9__CFError.cold.1
Functions:
~ __ZN20AppleTCONDP835DeviceC2Ej : 572 -> 580
~ __ZN20AppleTCONDP835Device24eventCmdPerformNextStageEPK14__CFDictionaryS2_Rh : 1032 -> 1028
~ _OUTLINED_FUNCTION_7 : 12 -> 28
~ _OUTLINED_FUNCTION_8 : 28 -> 20
~ _OUTLINED_FUNCTION_9 : 20 -> 32
~ _OUTLINED_FUNCTION_10 : 32 -> 12
~ __ZN20AppleTCONDP855Device11displayECIDEPKhm : 244 -> 236
~ __ZN20AppleTCONDP855Device18updateFWComponentsEPK14__CFDictionaryPh : 1008 -> 1040
~ __ZN25AppleTCONUpdateController5startEPK14__CFDictionaryPP9__CFError : 216 -> 168
~ __ZN25AppleTCONUpdateController16execCmdQueryInfoEPK14__CFDictionaryPS2_ : 292 -> 284
~ __ZN25AppleTCONUpdateController20execPerformNextStageEPK14__CFDictionary : 120 -> 112
~ __ZN20AppleTCONDP835Device7getECIDEPhj : 124 -> 128
~ _AppleTCONUpdaterIsDone : 184 -> 188

```

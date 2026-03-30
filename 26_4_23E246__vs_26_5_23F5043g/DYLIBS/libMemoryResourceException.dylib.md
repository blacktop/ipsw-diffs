## libMemoryResourceException.dylib

> `/usr/lib/libMemoryResourceException.dylib`

```diff

-314.100.11.0.0
-  __TEXT.__text: 0x1b064
+314.120.5.0.0
+  __TEXT.__text: 0x1b10c
   __TEXT.__auth_stubs: 0xcc0
   __TEXT.__objc_methlist: 0x15ac
   __TEXT.__const: 0x188
-  __TEXT.__cstring: 0x1f20
+  __TEXT.__cstring: 0x1f2e
   __TEXT.__oslogstring: 0xd18
   __TEXT.__gcc_except_tab: 0x3bc
   __TEXT.__ustring: 0xd0
   __TEXT.__unwind_info: 0x508
-  __TEXT.__objc_classname: 0x19e
-  __TEXT.__objc_methname: 0x3919
-  __TEXT.__objc_methtype: 0x836
-  __TEXT.__objc_stubs: 0x2c80
-  __DATA_CONST.__got: 0x280
+  __TEXT.__objc_classname: 0x19f
+  __TEXT.__objc_methname: 0x3971
+  __TEXT.__objc_methtype: 0x856
+  __TEXT.__objc_stubs: 0x2d00
+  __DATA_CONST.__got: 0x288
   __DATA_CONST.__const: 0xe58
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf58
+  __DATA_CONST.__objc_selrefs: 0xf78
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x38
   __AUTH_CONST.__auth_got: 0x670
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x27e0
-  __AUTH_CONST.__objc_const: 0x2f78
+  __AUTH_CONST.__cfstring: 0x2800
+  __AUTH_CONST.__objc_const: 0x2f98
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x278
+  __DATA.__objc_ivar: 0x27c
   __DATA.__data: 0x4f0
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_ivar: 0xc

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 81C58C26-CE3F-3429-9A3D-3E49054655E8
+  UUID: D9EDCE0F-40B1-39D9-AAA8-49CD9B38F255
   Functions: 493
-  Symbols:   2124
-  CStrings:  1687
+  Symbols:   2130
+  CStrings:  1696
 
Symbols:
+ _OBJC_CLASS_$_VMUAnalyticsEvent
+ _OBJC_IVAR_$_MemoryResourceException._analyticsEvent
+ ___block_literal_global.481
+ _objc_msgSend$addEnabledOption:value:
+ _objc_msgSend$populateInfoFromGraph:
+ _objc_msgSend$populateInfoFromTask:
+ _objc_msgSend$send
+ _objc_msgSend$taskPort
- ___block_literal_global.474
- _objc_msgSend$initWithTask:options:
Functions:
~ -[MemoryResourceException releaseAnalyzedTask] : 84 -> 180
~ +[MemoryResourceException resourceExceptionFromTask:error:] : 1508 -> 1560
~ -[MemoryResourceException _populateAddtionalMetadataWithOptions:timeoutSecs:] : 4164 -> 4212
~ -[MemoryResourceException initWithMetaDataDict:andMemoryGraph:withError:] : 3352 -> 3372
~ +[MemoryResourceException resourceExceptionFromLogFileHandle:error:] : 1112 -> 1132
~ -[MemoryResourceException .cxx_destruct] : 284 -> 308
~ _RMEGetDefaultLargeExemptedProcesses : 152 -> 104
~ _RMEPopulateDefaultPrefs : 1704 -> 1664
~ ___RMEIsAutoSubmitEnabled_block_invoke : 60 -> 56
CStrings:
+ "@\"VMUAnalyticsEvent\""
+ "@\"VMUTask\""
+ "T@\"VMUTask\",R,N,V_task"
+ "_analyticsEvent"
+ "addEnabledOption:value:"
+ "populateInfoFromGraph:"
+ "populateInfoFromTask:"
+ "send"
+ "taskPort"
- "TI,R,V_task"
- "initWithTask:options:"

```

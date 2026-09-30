## SessionFilterRecordingUpdater

> `/System/Library/PrivateFrameworks/MultitouchSessionFilterSupport.framework/XPCServices/SessionFilterRecordingUpdater.xpc/SessionFilterRecordingUpdater`

```diff

-8140.4.0.0.0
-  __TEXT.__text: 0x162c
-  __TEXT.__auth_stubs: 0x290
+9100.23.0.0.0
+  __TEXT.__text: 0x1758
+  __TEXT.__auth_stubs: 0x2a0
   __TEXT.__objc_stubs: 0x5c0
-  __TEXT.__objc_methlist: 0x2ac
+  __TEXT.__objc_methlist: 0x314
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0xd9
-  __TEXT.__gcc_except_tab: 0x11c
-  __TEXT.__objc_methname: 0x74f
-  __TEXT.__objc_classname: 0x94
-  __TEXT.__objc_methtype: 0x296
+  __TEXT.__objc_methname: 0x7ea
+  __TEXT.__cstring: 0xe1
+  __TEXT.__objc_classname: 0xad
+  __TEXT.__objc_methtype: 0x2ce
+  __TEXT.__gcc_except_tab: 0x114
   __TEXT.__oslogstring: 0xe2
-  __TEXT.__unwind_info: 0xe0
-  __DATA_CONST.__auth_got: 0x158
+  __TEXT.__unwind_info: 0xf0
+  __DATA_CONST.__auth_got: 0x160
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__const: 0xe0
-  __DATA_CONST.__cfstring: 0x40
-  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__cfstring: 0x60
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x638
-  __DATA.__objc_selrefs: 0x290
-  __DATA.__objc_ivar: 0x18
-  __DATA.__objc_data: 0x140
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA.__objc_const: 0x718
+  __DATA.__objc_selrefs: 0x2c0
+  __DATA.__objc_ivar: 0x1c
+  __DATA.__objc_data: 0x190
   __DATA.__data: 0x120
   __DATA.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 99DF6C05-F19F-3786-8B27-390649249B6E
-  Functions: 41
-  Symbols:   228
-  CStrings:  156
+  UUID: 698BB0F3-9A94-333B-ADA5-EA9F2E4B31A2
+  Functions: 49
+  Symbols:   245
+  CStrings:  171
 
Symbols:
+ -[MTSessionFilterManager .cxx_destruct]
+ -[MTSessionFilterManager debug]
+ -[MTSessionFilterManager filterEvent:fromService:]
+ -[MTSessionFilterManager init]
+ -[MTSessionFilterManager queue]
+ -[MTSessionFilterManager registerService:]
+ -[MTSessionFilterManager setQueue:]
+ -[MTSessionFilterManager unregisterService:]
+ GCC_except_table2
+ GCC_except_table8
+ MTLoggingAnalyticsFilterManager.__logObj
+ MTLoggingAnalyticsFilterManager.onceToken
+ MTLoggingCrownFilterManager.__logObj
+ MTLoggingCrownFilterManager.onceToken
+ MTLoggingRemoteFilterManager.__logObj
+ MTLoggingRemoteFilterManager.onceToken
+ OBJC_IVAR_$_MTSessionFilterManager._queue
+ _NSStringFromClass
+ _OBJC_CLASS_$_MTSessionFilterManager
+ _OBJC_METACLASS_$_MTSessionFilterManager
+ _Z41MTLoggingContinuousRecordingFilterManagerv.cold.1
+ __OBJC_$_INSTANCE_METHODS_MTSessionFilterManager
+ __OBJC_$_INSTANCE_VARIABLES_MTSessionFilterManager
+ __OBJC_$_PROP_LIST_MTSessionFilterManager
+ __OBJC_CLASS_RO_$_MTSessionFilterManager
+ __OBJC_METACLASS_RO_$_MTSessionFilterManager
+ __Z41MTLoggingContinuousRecordingFilterManagerv
+ __ZZ41MTLoggingContinuousRecordingFilterManagervE8__logObj
+ __ZZ41MTLoggingContinuousRecordingFilterManagervE9onceToken
+ ____Z41MTLoggingContinuousRecordingFilterManagerv_block_invoke
- GCC_except_table0
- GCC_except_table4
- MTLoggingContinuousRecordingFilterManager.cold.1
- _MTLoggingContinuousRecordingFilterManager
- __ZZ27MTLoggingCrownFilterManagerE8__logObj
- __ZZ27MTLoggingCrownFilterManagerE9onceToken
- __ZZ28MTLoggingRemoteFilterManagerE8__logObj
- __ZZ28MTLoggingRemoteFilterManagerE9onceToken
- __ZZ31MTLoggingAnalyticsFilterManagerE8__logObj
- __ZZ31MTLoggingAnalyticsFilterManagerE9onceToken
- __ZZ41MTLoggingContinuousRecordingFilterManagerE8__logObj
- __ZZ41MTLoggingContinuousRecordingFilterManagerE9onceToken
- ___MTLoggingContinuousRecordingFilterManager_block_invoke
- __block_literal_global.10
CStrings:
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@32@0:8@16@24"
+ "MTSessionFilterManager"
+ "Manager"
+ "T@\"NSDictionary\",R,N"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
+ "_queue"
+ "debug"
+ "filterEvent:fromService:"
+ "queue"
+ "registerService:"
+ "setQueue:"
+ "unregisterService:"
+ "v24@0:8@16"

```

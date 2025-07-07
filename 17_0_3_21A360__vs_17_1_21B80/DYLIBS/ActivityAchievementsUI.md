## ActivityAchievementsUI

> `/System/Library/PrivateFrameworks/ActivityAchievementsUI.framework/ActivityAchievementsUI`

```diff

-569.1.1.0.0
-  __TEXT.__text: 0x39e08
-  __TEXT.__auth_stubs: 0x1580
-  __TEXT.__objc_methlist: 0x17ac
-  __TEXT.__const: 0x680
-  __TEXT.__cstring: 0x19fa
-  __TEXT.__oslogstring: 0xbc6
+572.3.0.0.0
+  __TEXT.__text: 0x3b248
+  __TEXT.__auth_stubs: 0x15e0
+  __TEXT.__objc_methlist: 0x1884
+  __TEXT.__const: 0x690
+  __TEXT.__cstring: 0x1b7a
+  __TEXT.__oslogstring: 0xce3
   __TEXT.__gcc_except_tab: 0x1bc
-  __TEXT.__swift5_typeref: 0x3c6
-  __TEXT.__swift5_capture: 0x2d0
-  __TEXT.__swift5_fieldmd: 0x210
-  __TEXT.__constg_swiftt: 0x3dc
+  __TEXT.__swift5_typeref: 0x3cc
+  __TEXT.__swift5_capture: 0x2fc
+  __TEXT.__swift5_fieldmd: 0x228
+  __TEXT.__constg_swiftt: 0x44c
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0x2d3
+  __TEXT.__swift5_reflstr: 0x303
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x24
-  __TEXT.__unwind_info: 0x13cc
+  __TEXT.__unwind_info: 0x1424
   __TEXT.__eh_frame: 0x7e0
-  __TEXT.__objc_classname: 0x211
-  __TEXT.__objc_methname: 0x7028
-  __TEXT.__objc_methtype: 0xf09
-  __TEXT.__objc_stubs: 0x52c0
-  __DATA_CONST.__got: 0x2b0
+  __TEXT.__objc_classname: 0x248
+  __TEXT.__objc_methname: 0x710e
+  __TEXT.__objc_methtype: 0xf28
+  __TEXT.__objc_stubs: 0x5340
+  __DATA_CONST.__got: 0x2c8
   __DATA_CONST.__const: 0x598
-  __DATA_CONST.__objc_classlist: 0x88
+  __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x33e8
-  __DATA_CONST.__objc_selrefs: 0x19e8
+  __DATA_CONST.__objc_const: 0x34b0
+  __DATA_CONST.__objc_selrefs: 0x1a30
   __DATA_CONST.__objc_arraydata: 0x2d8
   __AUTH_CONST.__cfstring: 0x1a00
-  __AUTH_CONST.__objc_const: 0x4c8
-  __AUTH_CONST.__const: 0x11b0
+  __AUTH_CONST.__objc_const: 0x5e8
+  __AUTH_CONST.__const: 0x1270
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x2a8
   __AUTH_CONST.__objc_doubleobj: 0xc0
-  __AUTH_CONST.__auth_got: 0xad0
-  __AUTH.__objc_data: 0x8f0
+  __AUTH_CONST.__auth_got: 0xb00
+  __AUTH.__objc_data: 0xa10
   __AUTH.__data: 0x78
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x258
-  __DATA.__objc_superrefs: 0x70
-  __DATA.__objc_ivar: 0x254
-  __DATA.__data: 0x5e0
+  __DATA.__objc_classrefs: 0x268
+  __DATA.__objc_superrefs: 0x80
+  __DATA.__objc_ivar: 0x264
+  __DATA.__data: 0x5f0
   __DATA.__bss: 0x2d0
-  __DATA.__common: 0xc8
+  __DATA.__common: 0xd8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2342A5E8-5EA5-31B5-B784-335D9B80C0BD
-  Functions: 1184
-  Symbols:   2862
-  CStrings:  1856
+  UUID: 36CD91F7-AD0A-32C4-A42E-086A78A7647A
+  Functions: 1244
+  Symbols:   2946
+  CStrings:  1883
 
Symbols:
+ +[AAUICommandQueueRegistry sharedRegistry]
+ +[AAUICommandQueueTransaction sharedDevice]
+ -[AAUICommandQueueRegistry .cxx_destruct]
+ -[AAUICommandQueueRegistry _appDidBecomeActive]
+ -[AAUICommandQueueRegistry _appWillBecomeInactive]
+ -[AAUICommandQueueRegistry _locked_cacheCommandQueueIfNeeded]
+ -[AAUICommandQueueRegistry addCommandQueueTransaction:]
+ -[AAUICommandQueueRegistry commandQueue]
+ -[AAUICommandQueueRegistry init]
+ -[AAUICommandQueueRegistry removeCommandQueueTransaction:]
+ -[AAUICommandQueueRegistry sharedDevice]
+ -[AAUICommandQueueTransaction commandQueue]
+ -[AAUICommandQueueTransaction dealloc]
+ -[AAUICommandQueueTransaction init]
+ _OBJC_CLASS_$_AAUICommandQueueRegistry
+ _OBJC_CLASS_$_AAUICommandQueueTransaction
+ _OBJC_CLASS_$_NSOperationQueue
+ _OBJC_IVAR_$_AAUICommandQueueRegistry._cachedCommandQueue
+ _OBJC_IVAR_$_AAUICommandQueueRegistry._device
+ _OBJC_IVAR_$_AAUICommandQueueRegistry._lock
+ _OBJC_IVAR_$_AAUICommandQueueRegistry._transactions
+ _OBJC_IVAR_$_AAUIMetalBadgeRenderer._transaction
+ _OBJC_METACLASS_$_AAUICommandQueueRegistry
+ _OBJC_METACLASS_$_AAUICommandQueueTransaction
+ _UIApplicationDidEnterBackgroundNotification
+ _UIApplicationSignificantTimeChangeNotification
+ _UIApplicationWillEnterForegroundNotification
+ __OBJC_$_CLASS_METHODS_AAUICommandQueueRegistry
+ __OBJC_$_CLASS_METHODS_AAUICommandQueueTransaction
+ __OBJC_$_INSTANCE_METHODS_AAUICommandQueueRegistry
+ __OBJC_$_INSTANCE_METHODS_AAUICommandQueueTransaction
+ __OBJC_$_INSTANCE_VARIABLES_AAUICommandQueueRegistry
+ __OBJC_CLASS_RO_$_AAUICommandQueueRegistry
+ __OBJC_CLASS_RO_$_AAUICommandQueueTransaction
+ __OBJC_METACLASS_RO_$_AAUICommandQueueRegistry
+ __OBJC_METACLASS_RO_$_AAUICommandQueueTransaction
+ ___42+[AAUICommandQueueRegistry sharedRegistry]_block_invoke
+ ___swift_project_boxed_opaque_existential_0
+ __swift_dead_method_stub
+ __swift_stdlib_bridgeErrorToNSError
+ _block_copy_helper.22
+ _block_copy_helper.26
+ _block_copy_helper.33
+ _block_copy_helper.40
+ _block_copy_helper.56
+ _block_copy_helper.63
+ _block_copy_helper.70
+ _block_descriptor.24
+ _block_descriptor.28
+ _block_descriptor.35
+ _block_descriptor.42
+ _block_descriptor.58
+ _block_descriptor.65
+ _block_descriptor.72
+ _block_destroy_helper.23
+ _block_destroy_helper.27
+ _block_destroy_helper.34
+ _block_destroy_helper.41
+ _block_destroy_helper.57
+ _block_destroy_helper.64
+ _block_destroy_helper.71
+ _objc_msgSend$_locked_cacheCommandQueueIfNeeded
+ _objc_msgSend$addCommandQueueTransaction:
+ _objc_msgSend$commandQueue
+ _objc_msgSend$removeCommandQueueTransaction:
+ _objc_msgSend$sharedDevice
+ _objc_msgSend$sharedRegistry
+ _objectdestroy.54Tm
+ _sharedRegistry.onceToken
+ _sharedRegistry.registry
+ _swift_deletedMethodError
+ _swift_errorRetain
+ _symbolic SayypG
+ _symbolic So8NSObjectCSg
+ _symbolic _____yypG s23_ContiguousArrayStorageC
- +[AAUIMetalBadgeRenderer _commandQueueForDevice:]
- _OBJC_CLASS_$_NSMapTable
- _OBJC_IVAR_$_AAUIMetalBadgeRenderer._commandQueue
- __commandQueueForDevice:.deviceToCommandQueueTable
- __commandQueueForDevice:.lock
- _block_copy_helper.27
- _block_copy_helper.52
- _block_descriptor.29
- _block_descriptor.54
- _block_destroy_helper.28
- _block_destroy_helper.53
- _objc_msgSend$_commandQueueForDevice:
- _objc_msgSend$strongToStrongObjectsMapTable
- _symbolic SaySo14ACHAchievementCGz_Xx
CStrings:
+ "\x03"
+ "@\"AAUICommandQueueTransaction\""
+ "AAUICommandQueueRegistry"
+ "AAUICommandQueueTransaction"
+ "[AAUIAwardsDataProvider] App entered foreground, cycling data provider."
+ "[AAUIAwardsDataProvider] Failed to re-activate query during cycling: %@."
+ "[AAUIAwardsDataProvider] Received initial %ld achievements"
+ "[AAUIAwardsDataProvider] Significant time change, cycling data provider."
+ "[AAUICommandQueueRegistry] App backgrounded, clearing command queue"
+ "[AAUICommandQueueRegistry] App entered foreground with command queue: %@"
+ "[AAUICommandQueueRegistry] Creating new command queue"
+ "[AAUICommandQueueRegistry] Removed last command queue transaction, clearing command queue"
+ "_appDidBecomeActive"
+ "_appWillBecomeInactive"
+ "_cachedCommandQueue"
+ "_lock"
+ "_locked_cacheCommandQueueIfNeeded"
+ "_transaction"
+ "_transactions"
+ "addCommandQueueTransaction:"
+ "addObserverForName:object:queue:usingBlock:"
+ "commandQueue"
+ "initialAwardsBatchDelivered"
+ "mainQueue"
+ "observers"
+ "removeCommandQueueTransaction:"
+ "removeObserver:"
+ "sharedDevice"
+ "sharedRegistry"
+ "v16@?0@\"NSNotification\"8"
- "_commandQueue"
- "_commandQueueForDevice:"
- "strongToStrongObjectsMapTable"

```

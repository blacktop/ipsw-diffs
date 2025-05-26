## DashBoard

> `/System/Library/PrivateFrameworks/DashBoard.framework/DashBoard`

```diff

-332.13.2.0.0
-  __TEXT.__text: 0x15fbb0
+332.16.0.0.0
+  __TEXT.__text: 0x15fd18
   __TEXT.__auth_stubs: 0x3af0
-  __TEXT.__objc_methlist: 0xd94c
+  __TEXT.__objc_methlist: 0xd9a4
   __TEXT.__const: 0x28e4
   __TEXT.__cstring: 0xaaf6
   __TEXT.__gcc_except_tab: 0x1478

   __TEXT.__swift5_assocty: 0x1f0
   __TEXT.__swift5_proto: 0xb8
   __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__unwind_info: 0x57c8
+  __TEXT.__unwind_info: 0x57d4
   __TEXT.__eh_frame: 0xf50
   __TEXT.__objc_classname: 0x226a
-  __TEXT.__objc_methname: 0x2cd6e
-  __TEXT.__objc_methtype: 0x982e
-  __TEXT.__objc_stubs: 0x1c120
+  __TEXT.__objc_methname: 0x2ce50
+  __TEXT.__objc_methtype: 0x9850
+  __TEXT.__objc_stubs: 0x1c1a0
   __DATA_CONST.__got: 0xff0
   __DATA_CONST.__const: 0x30a8
   __DATA_CONST.__objc_classlist: 0x710

   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x5c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x36010
-  __DATA_CONST.__objc_selrefs: 0x8aa8
+  __DATA_CONST.__objc_const: 0x360a0
+  __DATA_CONST.__objc_selrefs: 0x8ac8
   __DATA_CONST.__objc_protorefs: 0x210
   __DATA_CONST.__objc_classrefs: 0x10d8
   __DATA_CONST.__objc_superrefs: 0x4e0

   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__auth_ptr: 0xd0
   __AUTH_CONST.__auth_got: 0x1d88
-  __AUTH.__objc_data: 0x5d48
+  __AUTH.__objc_data: 0x57a8
   __AUTH.__data: 0x10a0
-  __DATA.__objc_ivar: 0x114c
+  __DATA.__objc_ivar: 0x1154
   __DATA.__objc_data: 0xc0
   __DATA.__data: 0x56d0
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x1b48
-  __DATA.__common: 0x288
+  __DATA.__bss: 0x1a38
+  __DATA.__common: 0x280
+  __DATA_DIRTY.__objc_data: 0x5a0
+  __DATA_DIRTY.__bss: 0x110
+  __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7899
-  Symbols:   21500
-  CStrings:  10740
+  Functions: 7906
+  Symbols:   21520
+  CStrings:  10750
 
Symbols:
+ -[DBInstrumentClusterAppSceneViewController sceneIsForeground]
+ -[DBInstrumentClusterRootViewController sceneIsForeground]
+ -[DBLockOutController isInvalidated]
+ -[DBLockOutController setInvalidated:]
+ -[DBStatusBarStateProvider _resetTimeDateFormatter]
+ -[DBStatusBarStateProvider setTimeItemDateFormatter:]
+ -[DBStatusBarStateProvider timeItemDateFormatter]
+ GCC_except_table20
+ GCC_except_table54
+ _OBJC_IVAR_$_DBLockOutController._invalidated
+ _OBJC_IVAR_$_DBStatusBarStateProvider._timeItemDateFormatter
+ ___49-[DBStatusBarStateProvider _setupDNDStateService]_block_invoke.102
+ ___49-[DBStatusBarStateProvider _setupDNDStateService]_block_invoke.102.cold.1
+ ___block_literal_global.440
+ _objc_msgSend$_resetTimeDateFormatter
+ _objc_msgSend$currentLocale
+ _objc_msgSend$formatterForDateAsTimeNoAMPMWithLocale:
+ _objc_msgSend$sceneIsForeground
+ _objc_msgSend$setTimeItemDateFormatter:
+ _objc_msgSend$timeItemDateFormatter
- GCC_except_table29
- GCC_except_table45
- GCC_except_table53
- ___49-[DBStatusBarStateProvider _setupDNDStateService]_block_invoke.101
- ___49-[DBStatusBarStateProvider _setupDNDStateService]_block_invoke.101.cold.1
- ___block_literal_global.432
- _objc_msgSend$formatDateAsTimeNoAMPM:
- _objc_msgSend$resetFormattersIfNecessary
CStrings:
+ "\x14\x1f\x02"
+ "@\"NSDateFormatter\""
+ "@\"NSSet\"16@0:8"
+ "T@\"NSDateFormatter\",&,N,V_timeItemDateFormatter"
+ "T@\"NSSet\",?,R,C,N"
+ "_resetTimeDateFormatter"
+ "_timeItemDateFormatter"
+ "currentLocale"
+ "formatterForDateAsTimeNoAMPMWithLocale:"
+ "preferredBackgroundActivitiesToSuppress"
+ "sceneIsForeground"
+ "setTimeItemDateFormatter:"
+ "timeItemDateFormatter"
- "\x14\x1f\x01"
- "formatDateAsTimeNoAMPM:"
- "resetFormattersIfNecessary"

```

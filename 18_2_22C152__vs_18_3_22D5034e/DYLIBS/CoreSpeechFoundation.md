## CoreSpeechFoundation

> `/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation`

```diff

-3402.74.1.0.0
-  __TEXT.__text: 0xaa080
+3403.5.2.0.0
+  __TEXT.__text: 0xaa65c
   __TEXT.__auth_stubs: 0x1d70
-  __TEXT.__objc_methlist: 0xa238
-  __TEXT.__const: 0x788
+  __TEXT.__objc_methlist: 0xa3b0
+  __TEXT.__const: 0x798
+  __TEXT.__constg_swiftt: 0x240
   __TEXT.__swift5_typeref: 0x185
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_types: 0x1c
+  __TEXT.__cstring: 0x12abb
   __TEXT.__swift5_fieldmd: 0x128
-  __TEXT.__cstring: 0x12a86
-  __TEXT.__constg_swiftt: 0x240
   __TEXT.__swift5_reflstr: 0x84
-  __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_proto: 0x8
-  __TEXT.__swift5_types: 0x1c
-  __TEXT.__gcc_except_tab: 0x2b60
+  __TEXT.__gcc_except_tab: 0x2b80
   __TEXT.__oslogstring: 0xd5a8
   __TEXT.__dlopen_cstrs: 0x174
-  __TEXT.__unwind_info: 0x2c48
+  __TEXT.__unwind_info: 0x2cc0
   __TEXT.__eh_frame: 0xe8
-  __TEXT.__objc_classname: 0x18ad
-  __TEXT.__objc_methname: 0x1e0dc
-  __TEXT.__objc_methtype: 0x411e
-  __TEXT.__objc_stubs: 0xfb00
-  __DATA_CONST.__got: 0xec0
+  __TEXT.__objc_classname: 0x1924
+  __TEXT.__objc_methname: 0x1e420
+  __TEXT.__objc_methtype: 0x41ab
+  __TEXT.__objc_stubs: 0xfbc0
+  __DATA_CONST.__got: 0xed0
   __DATA_CONST.__const: 0x2160
-  __DATA_CONST.__objc_classlist: 0x618
+  __DATA_CONST.__objc_classlist: 0x630
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x170
+  __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6190
+  __DATA_CONST.__objc_selrefs: 0x6228
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x498
+  __DATA_CONST.__objc_superrefs: 0x4a0
   __DATA_CONST.__objc_arraydata: 0x1a8
   __AUTH_CONST.__auth_got: 0xed0
   __AUTH_CONST.__auth_ptr: 0x60
-  __AUTH_CONST.__const: 0x1470
+  __AUTH_CONST.__const: 0x14b0
   __AUTH_CONST.__cfstring: 0x87a0
-  __AUTH_CONST.__objc_const: 0x125a8
+  __AUTH_CONST.__objc_const: 0x129d8
   __AUTH_CONST.__objc_dictobj: 0x208
   __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_floatobj: 0x1b0
-  __AUTH.__objc_data: 0x240
-  __DATA.__objc_ivar: 0xb68
-  __DATA.__data: 0x1160
-  __DATA.__bss: 0x838
+  __AUTH.__objc_data: 0x330
+  __DATA.__objc_ivar: 0xb88
+  __DATA.__data: 0x1220
+  __DATA.__bss: 0x858
   __DATA_DIRTY.__objc_data: 0x3c68
-  __DATA_DIRTY.__data: 0x2c0
-  __DATA_DIRTY.__bss: 0x3c0
+  __DATA_DIRTY.__data: 0x2c8
   __DATA_DIRTY.__common: 0x68
+  __DATA_DIRTY.__bss: 0x3a8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4213
-  Symbols:   5609
-  CStrings:  8199
+  Functions: 4251
+  Symbols:   5652
+  CStrings:  8246
 
Symbols:
+ _OBJC_CLASS_$_CSEntityKitEventMonitor
+ _OBJC_CLASS_$_CSEntityKitManager
+ _OBJC_CLASS_$_CSEntityStatistics
+ _OBJC_METACLASS_$_CSEntityKitEventMonitor
+ _OBJC_METACLASS_$_CSEntityKitManager
+ _OBJC_METACLASS_$_CSEntityStatistics
CStrings:
+ "\x05"
+ "@\"CSEntityKitManager\""
+ "@\"CSEntityStatistics\""
+ "@\"NSSet\""
+ "CSEntityKitEventMonitor"
+ "CSEntityKitManager"
+ "CSEntityKitManagerDelegate"
+ "CSEntityStatistics"
+ "CSExclaveEntityKitProviding"
+ "T@\"CSEntityKitManager\",&,N,V_entityKitManager"
+ "T@\"CSEntityStatistics\",&,N,V_entityStatistics"
+ "T@\"NSSet\",R,N,V_entities"
+ "T@\"NSSet\",R,N,V_entitiesIsFacing"
+ "T@\"NSSet\",R,N,V_entitiesIsGazing"
+ "T@\"NSSet\",R,N,V_entitiesIsSpeaking"
+ "T@\"NSSet\",R,N,V_entitiesPresentInVicinity"
+ "T{os_unfair_lock_s=I},N,V_eventRWLock"
+ "_entities"
+ "_entitiesIsFacing"
+ "_entitiesIsGazing"
+ "_entitiesIsSpeaking"
+ "_entitiesPresentInVicinity"
+ "_entityKitManager"
+ "_entityStatistics"
+ "_eventRWLock"
+ "currentEntityStatistics"
+ "entities"
+ "entitiesIsFacing"
+ "entitiesIsGazing"
+ "entitiesIsSpeaking"
+ "entitiesPresentInVicinity"
+ "entityEventKitMonitorDidUpdate:"
+ "entityKitManager"
+ "entityKitManagerDidReceiveUpdate:"
+ "entityStatistics"
+ "eventRWLock"
+ "exclaveEntityKitProvider"
+ "isEntityInViewFacing"
+ "isEntityInViewGazing"
+ "isEntityInViewSpeaking"
+ "setEntityKitManager:"
+ "setEntityStatistics:"
+ "setEventRWLock:"
+ "updateEntityStatistics:"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "v24@0:8@\"CSEntityStatistics\"16"
+ "{os_unfair_lock_s=I}16@0:8"

```

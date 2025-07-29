## SiriTurnTakingManager

> `/System/Library/PrivateFrameworks/SiriTurnTakingManager.framework/SiriTurnTakingManager`

```diff

-3300.58.1.0.0
-  __TEXT.__text: 0x1f0d0
-  __TEXT.__auth_stubs: 0xfe0
+3301.6.1.0.0
+  __TEXT.__text: 0x1fa28
+  __TEXT.__auth_stubs: 0x1070
   __TEXT.__objc_methlist: 0xec
-  __TEXT.__const: 0xeb4
-  __TEXT.__cstring: 0x1fe8
+  __TEXT.__const: 0xec4
+  __TEXT.__cstring: 0x2138
   __TEXT.__swift5_typeref: 0x564
-  __TEXT.__swift5_fieldmd: 0x990
-  __TEXT.__constg_swiftt: 0x9ac
-  __TEXT.__swift5_reflstr: 0x495
+  __TEXT.__swift5_fieldmd: 0x9a8
+  __TEXT.__constg_swiftt: 0x9d0
+  __TEXT.__swift5_reflstr: 0x4b5
   __TEXT.__swift5_capture: 0x1c0
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_proto: 0xc8
   __TEXT.__swift5_types: 0x98
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__unwind_info: 0x7e8
+  __TEXT.__unwind_info: 0x7f8
   __TEXT.__eh_frame: 0x818
   __TEXT.__objc_methname: 0x4aa
   __DATA_CONST.__got: 0x150

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x818
   __DATA_CONST.__objc_selrefs: 0x230
-  __AUTH_CONST.__const: 0x18f0
-  __AUTH_CONST.__auth_got: 0x7f0
+  __AUTH_CONST.__const: 0x18f8
+  __AUTH_CONST.__auth_got: 0x838
   __AUTH.__data: 0x108
-  __AUTH.__objc_data: 0x300
+  __AUTH.__objc_data: 0x350
   __DATA.__objc_classrefs: 0x110
-  __DATA.__data: 0x908
+  __DATA.__data: 0x920
   __DATA.__bss: 0xf80
+  __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x2b8
-  __DATA_DIRTY.__data: 0x660
-  __DATA_DIRTY.__common: 0x58
+  __DATA_DIRTY.__data: 0x680
+  __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
   - /System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf

   - /System/Library/PrivateFrameworks/SiriMessageTypes.framework/SiriMessageTypes
   - /System/Library/PrivateFrameworks/SiriNLUTypes.framework/SiriNLUTypes
   - /System/Library/PrivateFrameworks/SiriOntology.framework/SiriOntology
+  - /System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C6F712BE-7D12-38D1-8B27-CDBD831CF8AF
-  Functions: 1038
-  Symbols:   896
-  CStrings:  237
+  UUID: DA977978-D2BB-3A3F-B96C-08379F673C10
+  Functions: 1047
+  Symbols:   908
+  CStrings:  244
 
Symbols:
+ _AFIsInternalInstall
+ __IVARS__TtC21SiriTurnTakingManager15AnnounceMatcher
+ _objc_retain_x28
+ _swift_endAccess
+ _swift_getSingletonMetadata
+ _swift_updateClassMetadata2
CStrings:
+ "AutoBugCapture#generateSnapshot ABC result: %{bool}d"
+ "Error %s when reading file %s"
+ "Using Cache - There is no activeTasks or executedTasks in SessionState for triggerless followup. Rejecting."
+ "announceTaskCache"
+ "assetPathGetter"
+ "identified announce type as %s - updating the cache so followup can also use this as announce task if needed"
+ "inputFeats - %@ - derivedInvocationType - %@"
+ "nc_asset_fetch_timeout"
+ "turntakingmanager"
- "Error reading file"
- "Unable to retrieve task from activeTasks or executedTasks in SessionState for triggerless followup. Rejecting."

```

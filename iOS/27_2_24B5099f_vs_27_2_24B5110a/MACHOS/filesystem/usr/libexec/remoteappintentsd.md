## remoteappintentsd

> `usr/libexec/remoteappintentsd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_reflstr`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_data`

```diff

-41.1.15.0.0
-  __TEXT.__text: 0x7b064
-  __TEXT.__auth_stubs: 0x2c80
-  __TEXT.__objc_stubs: 0xc40
+41.1.16.1.102
+  __TEXT.__text: 0x8175c
+  __TEXT.__auth_stubs: 0x2d00
+  __TEXT.__objc_stubs: 0xc80
   __TEXT.__objc_methlist: 0x3b4
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x2670
-  __TEXT.__swift5_typeref: 0x17fc
-  __TEXT.__cstring: 0x138a
+  __TEXT.__const: 0x2818
+  __TEXT.__swift5_typeref: 0x1822
+  __TEXT.__cstring: 0x13fa
   __TEXT.__objc_classname: 0x7b5
-  __TEXT.__objc_methname: 0x1485
+  __TEXT.__objc_methname: 0x14c5
   __TEXT.__objc_methtype: 0x645
-  __TEXT.__constg_swiftt: 0x11ec
+  __TEXT.__constg_swiftt: 0x126c
   __TEXT.__swift5_reflstr: 0xa74
-  __TEXT.__swift5_fieldmd: 0xc60
+  __TEXT.__swift5_fieldmd: 0xcbc
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_capture: 0x130c
-  __TEXT.__oslogstring: 0x212a
-  __TEXT.__swift5_assocty: 0x90
-  __TEXT.__swift5_proto: 0xb4
-  __TEXT.__swift5_types: 0x104
-  __TEXT.__swift_as_entry: 0x2a8
-  __TEXT.__swift_as_ret: 0x2e4
-  __TEXT.__swift_as_cont: 0x404
+  __TEXT.__swift5_capture: 0x1348
+  __TEXT.__oslogstring: 0x21b9
+  __TEXT.__swift5_assocty: 0xa8
+  __TEXT.__swift5_proto: 0xbc
+  __TEXT.__swift5_types: 0x108
+  __TEXT.__swift_as_entry: 0x2d4
+  __TEXT.__swift_as_ret: 0x314
+  __TEXT.__swift_as_cont: 0x490
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__unwind_info: 0x2990
-  __TEXT.__eh_frame: 0x63c8
-  __DATA_CONST.__const: 0x3a70
+  __TEXT.__unwind_info: 0x2bb0
+  __TEXT.__eh_frame: 0x6bc0
+  __DATA_CONST.__const: 0x3c48
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__auth_got: 0x1648
-  __DATA_CONST.__got: 0x848
-  __DATA_CONST.__auth_ptr: 0xc30
-  __DATA.__objc_const: 0x1768
-  __DATA.__objc_selrefs: 0x460
+  __DATA_CONST.__auth_got: 0x1688
+  __DATA_CONST.__got: 0x8a0
+  __DATA_CONST.__auth_ptr: 0xc88
+  __DATA.__objc_const: 0x1748
+  __DATA.__objc_selrefs: 0x470
   __DATA.__objc_data: 0x4a0
-  __DATA.__data: 0x2a60
-  __DATA.__common: 0x2c0
+  __DATA.__data: 0x2b30
+  __DATA.__common: 0x2f0
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
+  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata
   - /System/Library/PrivateFrameworks/LinkServices.framework/LinkServices
+  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2900
-  Symbols:   1148
-  CStrings:  572
+  Functions: 2996
+  Symbols:   1169
+  CStrings:  583
 
Symbols:
+ _$s12FeatureFlags02isA7EnabledySbAA0aB3Key_pF
+ _$s12FeatureFlags0aB3KeyMp
+ _$s12FeatureFlags0aB3KeyP6domains12StaticStringVvgTq
+ _$s12FeatureFlags0aB3KeyP7features12StaticStringVvgTq
+ _$s18AppIntentsServices06RemoteaB5ActorC11Distributed0fE0AAMc
+ _$s18AppIntentsServices06RemoteaB5ActorC7Network020NWSingletonPublishedE0AAMc
+ _$s18AppIntentsServices0bC0O10DeviceTypeO13homeAccessoryyA2EmFWC
+ _$s7Network10NWListenerC16debugDescriptionSSvg
+ _$s7Network10NWListenerC5StateO5readyyA2EmFWC
+ _$s7Network10NWListenerC5StateO5setupyA2EmFWC
+ _$s7Network10NWListenerC5StateO6failedyAeA7NWErrorOcAEmFWC
+ _$s7Network10NWListenerC5StateO7waitingyAeA7NWErrorOcAEmFWC
+ _$s7Network10NWListenerC5StateO9cancelledyA2EmFWC
+ _$s7Network10NWListenerC5StateOMa
+ _$s7Network10NWListenerC5stateAC5StateOvg
+ _$s7Network13NWActorSystemC8listenerAA10NWListenerCSgvg
+ _$sScT2eeoiySbScTyxq_G_ABtFZ
+ _$ss12StaticStringVMn
+ _OBJC_CLASS_$_MCProfileConnection
+ _swift_checkMetadataState
+ _swift_getTupleTypeMetadata2
CStrings:
+ "%s: Listener activated for %s, republishOnWake: %{bool}d"
+ "%s: already started (%s), start() called twice?"
+ "%s: failed to publish actor over %s: %@"
+ "%s: republish requested over %s, will republish: %s current state: %s, actorSystem.listener: %s"
+ "%s: republish requested while %s, joining the in-flight publish"
+ "%s: republish requested while %s, nothing to republish"
+ "%s: republishing actor failed, retrying once: %@"
+ "%s: stopping after a failed publish"
+ "%sHome device pairing management enabled. Allowed: %{bool}d"
+ "AppIntentsServices"
+ "Joining existing listener for %s"
+ "Listener for %s failed to publish, discarding it: %@"
+ "applicationID"
+ "cancelled"
+ "failed"
+ "initial"
+ "isPairingWithHomeDevicesAllowed"
+ "published"
+ "publishing"
+ "republishListenerOnRapportWake"
+ "sharedConnection"
- "%s: actor already published, start() called twice?"
- "%s: already started publishing actor, start() called twice?"
- "%sHome device pairing management disabled. Default to allow: true."
- "BUG? A listener was already active for %s"
- "ERROR: %@"
- "Rapport service %s has already been initialized. Rapport bug?"
- "Rapport service %s initialization completed, success: %{bool}d"
- "Terminus service %s has already been initialized"
- "Terminus service %s initialization completed, success: %{bool}d"
- "initializedServices"
```

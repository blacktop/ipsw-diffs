## MenstrualCyclesAppPlugin

> `/System/Library/Health/FeedItemPlugins/MenstrualCyclesAppPlugin.healthplugin/MenstrualCyclesAppPlugin`

```diff

-5200.1.9.1.2
-  __TEXT.__text: 0x48c420
-  __TEXT.__auth_stubs: 0x9420
-  __TEXT.__objc_methlist: 0x3b4c
-  __TEXT.__const: 0x1d904
-  __TEXT.__cstring: 0x20e68
-  __TEXT.__constg_swiftt: 0xfd64
-  __TEXT.__swift5_typeref: 0x925e
-  __TEXT.__swift5_builtin: 0x398
-  __TEXT.__swift5_reflstr: 0xda83
-  __TEXT.__swift5_fieldmd: 0xb498
-  __TEXT.__swift5_assocty: 0x17c8
-  __TEXT.__oslogstring: 0xa321
-  __TEXT.__swift5_capture: 0x30d4
-  __TEXT.__swift5_proto: 0x13ec
-  __TEXT.__swift5_types: 0xc20
-  __TEXT.__swift5_protos: 0x148
+5200.1.15.1.2
+  __TEXT.__text: 0x494c7c
+  __TEXT.__auth_stubs: 0x95f0
+  __TEXT.__objc_methlist: 0x3b64
+  __TEXT.__const: 0x1de34
+  __TEXT.__cstring: 0x21038
+  __TEXT.__constg_swiftt: 0xfef4
+  __TEXT.__swift5_typeref: 0x93b8
+  __TEXT.__swift5_builtin: 0x3ac
+  __TEXT.__swift5_reflstr: 0xdb43
+  __TEXT.__swift5_fieldmd: 0xb5f4
+  __TEXT.__swift5_assocty: 0x17e8
+  __TEXT.__oslogstring: 0xa4e1
+  __TEXT.__swift5_capture: 0x30e4
+  __TEXT.__swift5_proto: 0x143c
+  __TEXT.__swift5_types: 0xc40
+  __TEXT.__swift5_protos: 0x14c
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0xc778
-  __TEXT.__eh_frame: 0x739c
+  __TEXT.__unwind_info: 0xc918
+  __TEXT.__eh_frame: 0x7524
   __TEXT.__objc_classname: 0x47b
-  __TEXT.__objc_methname: 0xbe67
+  __TEXT.__objc_methname: 0xbe6c
   __TEXT.__objc_methtype: 0x334e
   __TEXT.__objc_stubs: 0xc0
-  __DATA_CONST.__got: 0x28d8
-  __DATA_CONST.__const: 0x8e8
-  __DATA_CONST.__objc_classlist: 0x9b8
+  __DATA_CONST.__got: 0x2948
+  __DATA_CONST.__const: 0x8f0
+  __DATA_CONST.__objc_classlist: 0x9c8
   __DATA_CONST.__objc_catlist2: 0x40
   __DATA_CONST.__objc_protolist: 0x2d0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2928
   __DATA_CONST.__objc_protorefs: 0x170
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x4a18
-  __AUTH_CONST.__auth_ptr: 0x3aa0
-  __AUTH_CONST.__const: 0x13850
+  __AUTH_CONST.__auth_got: 0x4b00
+  __AUTH_CONST.__auth_ptr: 0x3ac8
+  __AUTH_CONST.__const: 0x13a80
   __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0x18380
-  __AUTH.__objc_data: 0xda20
-  __AUTH.__data: 0xb890
+  __AUTH_CONST.__objc_const: 0x18528
+  __AUTH.__objc_data: 0xda70
+  __AUTH.__data: 0xbaf0
   __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0xb678
+  __DATA.__data: 0xb848
   __DATA.__objc_stublist: 0xd0
-  __DATA.__bss: 0x1ec10
-  __DATA.__common: 0xbf8
+  __DATA.__bss: 0x1f590
+  __DATA.__common: 0xc18
   __DATA_DIRTY.__objc_data: 0x2890
   __DATA_DIRTY.__data: 0x4670
   __DATA_DIRTY.__bss: 0x4680

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 17816
-  Symbols:   716
-  CStrings:  5765
+  Functions: 17949
+  Symbols:   719
+  CStrings:  5781
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
CStrings:
+ "Cannot perform work without a HealthPlatformOrchestrationContext, ignoring context: %!s(MISSING)"
+ "Cannot perform work without a health store, ignoring context: %!s(MISSING)"
+ "No pregnancy information in medical id, do not need to show feed item"
+ "ReviewPregnancyInMedicalIDTileDismissalInputSignal"
+ "Should not show on iPad, do not need to show feed item."
+ "Tile was dismissed in the last three months, not showing tile"
+ "[%!s(MISSING)] Error setting dismissal date: %!s(MISSING)"
+ "[%!s(MISSING)] Failed decoding user data: %!s(MISSING)"
+ "[%!s(MISSING)] No model. creating a new feed item."
+ "[%!s(MISSING)] Sample UUID from user data was nil"
+ "[%!s(MISSING)] Set dismissal date success %!{(MISSING)bool}d, error %!{(MISSING)public}s"
+ "[%!{(MISSING)public}s] Couldn't get date for last dismissal date for tile, %!s(MISSING)"
+ "_PMedicalIDUpdateFeedItem.Alert"
+ "_TtC24MenstrualCyclesAppPlugin50ReviewPregnancyInMedicalIDTileDismissalInputSignal"
+ "_TtCC24MenstrualCyclesAppPlugin50ReviewPregnancyInMedicalIDTileDismissalInputSignal12ObserverShim"
+ "lastDismissedDate"
+ "observerShim"
+ "protectedState"
+ "setData:forKey:completion:"
- "NO pregnancy information in medical id, do not need to show feed item"
- "PMedicalIDUpdateFeedItem"
- "[%!{(MISSING)sensitive}s] Error setting dismissal date: %!s(MISSING)"
- "setDate:forKey:error:"

```

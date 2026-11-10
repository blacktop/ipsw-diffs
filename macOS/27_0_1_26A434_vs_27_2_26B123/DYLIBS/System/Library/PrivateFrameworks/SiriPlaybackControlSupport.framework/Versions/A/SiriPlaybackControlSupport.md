## SiriPlaybackControlSupport

> `/System/Library/PrivateFrameworks/SiriPlaybackControlSupport.framework/Versions/A/SiriPlaybackControlSupport`

```diff

-3600.26.17.0.0
-  __TEXT.__text: 0x7f148
+3605.17.1.0.0
+  __TEXT.__text: 0x8210c
   __TEXT.__objc_methlist: 0x184
-  __TEXT.__const: 0x4b32
-  __TEXT.__swift5_typeref: 0x18d6
-  __TEXT.__swift5_capture: 0x1278
-  __TEXT.__oslogstring: 0x5b3c
-  __TEXT.__swift5_fieldmd: 0x2190
-  __TEXT.__constg_swiftt: 0x1d24
+  __TEXT.__const: 0x4c62
+  __TEXT.__swift5_typeref: 0x19c6
+  __TEXT.__swift5_capture: 0x1388
+  __TEXT.__oslogstring: 0x5dac
+  __TEXT.__swift5_fieldmd: 0x21f0
+  __TEXT.__constg_swiftt: 0x1db0
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0x18a0
+  __TEXT.__swift5_reflstr: 0x18d0
   __TEXT.__swift5_assocty: 0x508
   __TEXT.__cstring: 0x2747
-  __TEXT.__swift5_protos: 0x50
-  __TEXT.__swift5_proto: 0x310
-  __TEXT.__swift5_types: 0x17c
+  __TEXT.__swift5_protos: 0x58
+  __TEXT.__swift5_proto: 0x318
+  __TEXT.__swift5_types: 0x180
   __TEXT.__swift5_mpenum: 0x40
-  __TEXT.__unwind_info: 0x1da0
-  __TEXT.__eh_frame: 0x1088
+  __TEXT.__unwind_info: 0x1e08
+  __TEXT.__eh_frame: 0x10a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3e0
+  __DATA_CONST.__objc_selrefs: 0x408
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x7778
+  __AUTH_CONST.__const: 0x7ab8
   __AUTH_CONST.__objc_const: 0xd20
-  __AUTH_CONST.__auth_got: 0xd78
-  __AUTH_CONST.__auth_ptr: 0x6a0
+  __AUTH_CONST.__auth_got: 0xd88
+  __AUTH_CONST.__auth_ptr: 0x6b8
   __AUTH.__objc_data: 0x2a8
-  __AUTH.__data: 0x11c8
-  __DATA.__data: 0x1000
+  __AUTH.__data: 0x11d0
+  __DATA.__data: 0x1038
   __DATA.__bss: 0x5a80
   __DATA.__common: 0xd0
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4083
-  Symbols:   1127
-  CStrings:  666
+  Functions: 4171
+  Symbols:   1155
+  CStrings:  672
 
Symbols:
+ _HMAccessoryCategoryTypeTelevisionSetTopBox
+ _HMAccessoryCategoryTypeTelevisionStreamingStick
+ _NSSelectorFromString
+ _OBJC_CLASS_$_HMMediaGroup
+ __swift_closure_destructor.113Tm
+ __swift_closure_destructor.53Tm
+ _kMRMediaRemoteCommandInfoPreferredIntervalsKey
+ _objc_msgSend$audioDestinationIdentifier
+ _objc_msgSend$audioGroupsController
+ _objc_msgSend$destinationIdentifiers
+ _objc_msgSend$groups
+ _objc_msgSend$identifier
+ _objc_msgSend$performSelector:
+ _objc_msgSend$respondsToSelector:
+ _objc_retainAutorelease
+ _symbolic $s26SiriPlaybackControlSupport14AudioGroupTypeP
+ _symbolic $s26SiriPlaybackControlSupport15MediaSystemTypeP
+ _symbolic SDySSypG
+ _symbolic SDy_____ypGIegr_ s11AnyHashableV
+ _symbolic Say_____GIegg_ 26SiriPlaybackControlSupport16SupportedCommandV
+ _symbolic SdSgIegy_
+ _symbolic _____ 26SiriPlaybackControlSupport16SupportedCommandV
+ _symbolic ______p 26SiriPlaybackControlSupport14AudioGroupTypeP
+ _symbolic ______p 26SiriPlaybackControlSupport15MediaSystemTypeP
+ _symbolic ______pSg 26SiriPlaybackControlSupport14AudioGroupTypeP
+ _symbolic ______pSg 26SiriPlaybackControlSupport15MediaSystemTypeP
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 26SiriPlaybackControlSupport16SupportedCommandV
+ _symbolic _____y______pG s23_ContiguousArrayStorageC 26SiriPlaybackControlSupport14AudioGroupTypeP
+ _symbolic _____y______pG s23_ContiguousArrayStorageC 26SiriPlaybackControlSupport15MediaSystemTypeP
+ _type_layout_string 26SiriPlaybackControlSupport16SupportedCommandV
- __swift_closure_destructor.107Tm
- __swift_closure_destructor.47Tm
CStrings:
+ "Accessory %s is a speaker in surround system %s"
+ "Accessory %s is in no media system and has no audio destination identifier"
+ "Accessory %s matched none of the %ld audio group(s)"
+ "HomeEntityMatchingService#accessories %s has deviceType %{public}s, which the predicate's %{public}s does not ask for, skipping..."
+ "HomeEntityMatchingService#accessories %s has no DeviceCategory for homekitType %{public}s, so it is untargetable by any predicate. Add the type to DeviceCategory.homekitToCategoryMap. Skipping..."
+ "PlaybackControlling#timeSkipFallbackInterval default implementation should not be used"
+ "Track skip unsupported for now playing app, falling back to a %fs time skip"
- "HomeEntityMatchingService#accessories deviceType doesn't match predicate, skipping..."
```

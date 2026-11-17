## TextInputUI

> `/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI`

```diff

-9127.2.6.0.0
-  __TEXT.__text: 0x14bf8c
-  __TEXT.__objc_methlist: 0x10d04
+9127.2.11.0.0
+  __TEXT.__text: 0x14e4d4
+  __TEXT.__objc_methlist: 0x10d2c
   __TEXT.__dlopen_cstrs: 0x3f1
-  __TEXT.__const: 0x423e
-  __TEXT.__swift5_typeref: 0x1f2c
+  __TEXT.__const: 0x427e
+  __TEXT.__swift5_typeref: 0x1f54
   __TEXT.__swift5_capture: 0x6ec
-  __TEXT.__cstring: 0xdb5d
+  __TEXT.__cstring: 0xdb8d
   __TEXT.__constg_swiftt: 0x1ad4
   __TEXT.__swift5_reflstr: 0xe15
   __TEXT.__swift5_assocty: 0x3a0
   __TEXT.__swift5_fieldmd: 0xff0
   __TEXT.__swift5_builtin: 0x17c
-  __TEXT.__oslogstring: 0x6bd2
+  __TEXT.__oslogstring: 0x6cfc
   __TEXT.__swift5_proto: 0x1c0
   __TEXT.__swift5_types: 0x170
   __TEXT.__swift_as_entry: 0x88

   __TEXT.__swift5_mpenum: 0x1c
   __TEXT.__swift5_protos: 0xc
   __TEXT.__ustring: 0x258
-  __TEXT.__unwind_info: 0x5730
+  __TEXT.__unwind_info: 0x5748
   __TEXT.__eh_frame: 0x227c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x2c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xacd0
+  __DATA_CONST.__objc_selrefs: 0xacf0
   __DATA_CONST.__objc_protorefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x468
   __DATA_CONST.__objc_arraydata: 0xb18
-  __DATA_CONST.__got: 0x1700
-  __AUTH_CONST.__const: 0x33a0
-  __AUTH_CONST.__cfstring: 0xee20
-  __AUTH_CONST.__objc_const: 0x1ae68
+  __DATA_CONST.__got: 0x1720
+  __AUTH_CONST.__const: 0x33c0
+  __AUTH_CONST.__cfstring: 0xee40
+  __AUTH_CONST.__objc_const: 0x1ae98
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_arrayobj: 0x2b8
   __AUTH_CONST.__objc_doubleobj: 0x1a0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_floatobj: 0xe0
-  __AUTH_CONST.__auth_got: 0x1e68
+  __AUTH_CONST.__auth_got: 0x1ea0
   __AUTH.__objc_data: 0x3bb8
   __AUTH.__data: 0x1040
-  __DATA.__objc_ivar: 0x12b0
-  __DATA.__data: 0x2ed8
+  __DATA.__objc_ivar: 0x12b4
+  __DATA.__data: 0x2f08
   __DATA.__common: 0x290
   __DATA_DIRTY.__objc_data: 0x20a8
   __DATA_DIRTY.__data: 0x2e8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7368
-  Symbols:   11236
-  CStrings:  2792
+  Functions: 7376
+  Symbols:   11247
+  CStrings:  2796
 
Symbols:
+ +[TUIGenmojiCandidate prefersArchivedResultSetCoding]
+ +[TUIKeyplaneView reuseActionForParentUnchanged:placementUnchanged:appliedConstraintsActive:appliedAnchorsStillLive:]
+ -[TUIKeyboardTrackingProvider sceneSizesMatch]
+ -[TUIKeyplane widenLeftControlColumnInKeyRow:]
+ -[TUIPasteboardSnapshot concealment]
+ -[TUISystemInputAssistantView cancelledTransitionToState:]
+ _OBJC_IVAR_$_TUIPasteboardSnapshot._concealment
+ _TIGetConsiderEmpordaPasswordProviderValue.onceToken
+ _TIInputModeGetLanguageWithRegion
+ ___TIGetConsiderEmpordaPasswordProviderValue_block_invoke
+ _symbolic _____Sg 10Foundation6LocaleV6RegionV
+ _symbolic _____Sg 10Foundation6LocaleV6ScriptV
+ _symbolic _____Sg_ABt 10Foundation6LocaleV6RegionV
+ _symbolic _____Sg_ABt 10Foundation6LocaleV6ScriptV
- +[TUIKeyplaneView reuseActionForParentUnchanged:placementUnchanged:appliedAnchorsStillLive:]
- -[TUIKeyboardTrackingProvider screenBoundsMatch]
- _CGSizeNearlyEqualToSizeWithTolerance
CStrings:
+ "<%@: itemCount=%lu hasStrings=%@ hasWebURLs=%@ hasFiles=%@ hasImages=%@ concealment=%ld>"
+ "Cancelled paste candidate generation due to concealed pasteboard"
+ "ConsiderEmpordaPasswordProvider"
+ "EmojiRemoteView Reanchored: key=%{public}@ placement changed or constraints deactivated under a cached remote view — rebuilding its constraints in %p (constraintsActive %d, hadWindow %d→%d, sameWindow %d, inKeyplaneTree %d→%d, extents %ld/%ld/%ld→%ld/%ld/%ld, offsets %.1f/%.1f→%.1f/%.1f)"
+ "Originator is Emporda and ConsiderEmpordaPasswordProvider is off; treating pasteboard as non-credential-provider"
+ "Pasteboard explicitly not concealed; skipping credential provider gate"
- "<%@: itemCount=%lu hasStrings=%@ hasWebURLs=%@ hasFiles=%@ hasImages=%@>"
- "EmojiRemoteView Reanchored: key=%{public}@ placement changed under a cached remote view — rebuilding its constraints in %p (hadWindow %d→%d, sameWindow %d, inKeyplaneTree %d→%d, extents %ld/%ld/%ld→%ld/%ld/%ld, offsets %.1f/%.1f→%.1f/%.1f)"
```

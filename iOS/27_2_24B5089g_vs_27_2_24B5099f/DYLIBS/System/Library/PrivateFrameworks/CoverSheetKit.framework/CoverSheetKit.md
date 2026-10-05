## CoverSheetKit

> `/System/Library/PrivateFrameworks/CoverSheetKit.framework/CoverSheetKit`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-159.2.1.0.0
-  __TEXT.__text: 0x39f3c
+159.2.4.0.0
+  __TEXT.__text: 0x3a4b8
   __TEXT.__objc_methlist: 0x2a8c
-  __TEXT.__const: 0x243c
+  __TEXT.__const: 0x245c
   __TEXT.__cstring: 0x867
   __TEXT.__gcc_except_tab: 0x204
   __TEXT.__dlopen_cstrs: 0x50
-  __TEXT.__oslogstring: 0x555
+  __TEXT.__oslogstring: 0x855
   __TEXT.__ustring: 0x14
   __TEXT.__constg_swiftt: 0xba4
   __TEXT.__swift5_typeref: 0x1c9d

   __TEXT.__swift5_capture: 0x68
   __TEXT.__swift5_proto: 0xa4
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x1630
+  __TEXT.__unwind_info: 0x1628
   __TEXT.__eh_frame: 0x238
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f70
+  __DATA_CONST.__objc_selrefs: 0x1f80
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__got: 0x5a8
   __AUTH_CONST.__const: 0xcd0
   __AUTH_CONST.__cfstring: 0x6c0
-  __AUTH_CONST.__objc_const: 0x4fa8
+  __AUTH_CONST.__objc_const: 0x4fc8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0xb18
   __AUTH.__objc_data: 0x4a8
   __AUTH.__data: 0x200
-  __DATA.__objc_ivar: 0x2cc
+  __DATA.__objc_ivar: 0x2d0
   __DATA.__data: 0x860
   __DATA.__common: 0xc0
   __DATA_DIRTY.__objc_data: 0xad8
-  __DATA_DIRTY.__data: 0x6a8
-  __DATA_DIRTY.__bss: 0x788
+  __DATA_DIRTY.__data: 0x6a0
+  __DATA_DIRTY.__bss: 0x778
   __DATA_DIRTY.__common: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1763
+  Functions: 1762
   Symbols:   2018
-  CStrings:  121
+  CStrings:  124
 
Symbols:
+ _OBJC_IVAR_$_CSProminentTextElementView._lastLoggedLabelRect
- ___57-[CSProminentTextElementView insertPrefixViews:animated:]_block_invoke_4
Functions:
~ -[CSProminentTimeView layoutSubviews] : 868 -> 872
~ -[CSProminentTextElementView layoutSubviews] : 356 -> 1104
~ -[CSProminentDisplayView layoutSubviews] : 2092 -> 2724
- -[CSProminentDisplayView layoutSubviews].cold.1
~ -[CSProminentDisplayViewController setDateTimeAlignment:] : 260 -> 376
~ ___57-[CSProminentTextElementView insertPrefixViews:animated:]_block_invoke : 460 -> 572
CStrings:
+ "CSProminentTimeView textLabel is not centered with timeViewFrame: %{public}@, textLabel frame: %{public}@, measurementFont: %{public}@, labelSize: %{public}@."
+ "Setting date and time textAlignment to: %lu, reachedTimeView: %{bool}u, reachedSubtitleView: %{bool}u"
+ "Skipping setting time frame due to applied transform: %{public}@"
+ "Subtitle box is not centered in prominentDisplayView. boundingRect: %{public}@, subtitleFrame: %{public}@, appliedFrame: %{public}@, usesEditingLayout: %{bool}u."
+ "Text element is switching to stack layout permanently. elementType: %lu, bounds: %{public}@."
+ "Text element label is not centered despite center alignment. elementType: %lu, bounds: %{public}@, label: %{public}@, measured: %{public}@, contentIsStack: %{bool}u, stack: %{public}@, leadingSpacer: %{public}@, contentStack: %{public}@, trailingSpacer: %{public}@, font: %{public}@, contentSizeCategory: %{public}@, textLength: %lu, text: %@."
+ "Time is not centered in prominentDisplayView, boundingRect: %{public}@, timeFrame: %{public}@, timeView frame: %{public}@, adaptsTextHeight: %{bool}u, calculated textHeight: %f, baseFont: %{public}@."
- "CSProminentTimeView textLabel is not centered with timeViewFrame: %@, textLabel frame: %@, measurementFont: %@, labelSize: %@."
- "Setting date and time textAlignment to: %lu"
- "Skipping setting time frame due to applied transform: %@"
- "Time is not centered in prominentDisplayView, timeView frame: %@, adaptsTextHeight: %{bool}u, calculated textHeight: %f, baseFont: %@."
```

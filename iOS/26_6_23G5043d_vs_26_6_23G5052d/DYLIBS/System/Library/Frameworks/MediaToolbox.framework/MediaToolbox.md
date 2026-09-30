## MediaToolbox

> `/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`

```diff

-  __TEXT.__text: 0xfa5348
+  __TEXT.__text: 0xfa5df0
   __TEXT.__auth_stubs: 0xb640
   __TEXT.__objc_methlist: 0x250c
   __TEXT.__const: 0x2bc30
-  __TEXT.__cstring: 0x13321c
-  __TEXT.__oslogstring: 0x1518a4
+  __TEXT.__cstring: 0x133236
+  __TEXT.__oslogstring: 0x151a73
   __TEXT.__ustring: 0x23e
   __TEXT.__gcc_except_tab: 0x18c8
   __TEXT.__dlopen_cstrs: 0x21e
-  __TEXT.__unwind_info: 0x142c0
+  __TEXT.__unwind_info: 0x142d0
   __TEXT.__eh_frame: 0x1b8
   __TEXT.__objc_classname: 0x82d
   __TEXT.__objc_methname: 0x6d95

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 49138
-  Symbols:   132258
-  CStrings:  67805
+  Functions: 49140
+  Symbols:   132268
+  CStrings:  67810
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ _MTAudioProcessingTapAQCanBeAddedToSubmix
+ _subAQ_isEligibleForSubmix
CStrings:
+ "((( AudioProcessingTapServer(XPC) ))) %s: Tap %p / ATSubmixTap %p / AQ %p %sassigned / AQ count %d / "
+ "<<<< FAQ >>>> %s: [%p:%p] %s A subAQ with an AQ that can't be added to a submix unexpectedly has a non-NULL submixID and a non-NULL MTAudioProcessingTap"
+ "<<<< FAQ >>>> %s: [%p:%p] %s decodable format('%c%c%c%c') is ineligible for assignment to a submix tap"
+ "<<<< FAQ >>>> %s: [%p:%p] %s passthrough format('%c%c%c%c') is ineligible for assignment to a submix tap"
+ "subAQ_isEligibleForSubmix"

```

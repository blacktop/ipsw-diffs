## caraccessoryd

> `/usr/libexec/caraccessoryd`

```diff

-337.8.3.0.0
-  __TEXT.__text: 0x225f0
-  __TEXT.__auth_stubs: 0xf50
-  __TEXT.__objc_stubs: 0x1f40
+337.11.1.0.0
+  __TEXT.__text: 0x22300
+  __TEXT.__auth_stubs: 0xea0
+  __TEXT.__objc_stubs: 0x1f20
   __TEXT.__objc_methlist: 0xc48
-  __TEXT.__const: 0x2f8
+  __TEXT.__const: 0x308
   __TEXT.__cstring: 0xdb3
   __TEXT.__gcc_except_tab: 0x120
-  __TEXT.__objc_methname: 0x327b
-  __TEXT.__oslogstring: 0x301b
+  __TEXT.__objc_methname: 0x3281
+  __TEXT.__oslogstring: 0x303b
   __TEXT.__objc_classname: 0x309
   __TEXT.__objc_methtype: 0x1043
   __TEXT.__swift5_typeref: 0x3aa

   __TEXT.__swift5_reflstr: 0x183
   __TEXT.__swift5_fieldmd: 0x1c8
   __TEXT.__swift5_types: 0x18
-  __TEXT.__unwind_info: 0x6a8
+  __TEXT.__unwind_info: 0x6b0
   __TEXT.__eh_frame: 0x138
-  __DATA_CONST.__auth_got: 0x7b8
+  __DATA_CONST.__auth_got: 0x760
   __DATA_CONST.__got: 0x3d0
   __DATA_CONST.__auth_ptr: 0x80
   __DATA_CONST.__const: 0xb20

   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0x60
   __DATA.__objc_const: 0x3ab0
-  __DATA.__objc_selrefs: 0xca8
+  __DATA.__objc_selrefs: 0xca0
   __DATA.__objc_ivar: 0xb8
   __DATA.__objc_data: 0x868
   __DATA.__data: 0xe28

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 683
-  Symbols:   1952
-  CStrings:  1066
+  Functions: 680
+  Symbols:   1938
+  CStrings:  1064
 
Symbols:
+ -[CAFDCarDataServiceAgent _removeRegistration:instanceIDs:priority:withResponse:].cold.2
+ _$sSo21CAFNowPlayingSnapshotC6titles11artworkData15mediaSourceType0gH10Identifier0E5Token0g9ItemImageK00eI09multicastABSaySSG_10Foundation0F0VSgSo08CAFMediah8SemanticI0VSSS2iSo0ab7ArtworkI0VSitcfC
+ _CAFRequestForcedPriority
+ ___52-[CAFDCarDataServiceAgent registrationsForPluginID:]_block_invoke
- _$s13caraccessoryd19CAFDNowPlayingAgentC18accessoryDidUpdate_17receivedAllValuesySo12CAFAccessoryC_SbtFTm
- _$sSo21CAFNowPlayingSnapshotC6titles11artworkData15mediaSourceType0gH10Identifier0E5Token0g9ItemImageK0ABSaySSG_10Foundation0F0VSgSo08CAFMediah8SemanticI0VSSS2itcfC
- _CAFCopyImageSourceAndGetSizeFromData
- _CAFImageDataByCenteringImageOnPlatterWithSize
- _CFDataCreateMutable
- _CGBitmapContextCreate
- _CGBitmapContextCreateImage
- _CGColorCreateSRGB
- _CGColorRelease
- _CGColorSpaceCreateWithName
- _CGColorSpaceRelease
- _CGContextDrawImage
- _CGContextFillRect
- _CGContextRelease
- _CGContextSetFillColorWithColor
- _OUTLINED_FUNCTION_14
- _kCGColorSpaceSRGB
- _objc_msgSend$dataWithData:
CStrings:
+ "Force Remove registration pluginID: %!{(MISSING)public}@ instanceIDs count %!{(MISSING)public}lu with priority: %!{(MISSING)public}@"
+ "Found media item with identifier %!{(MISSING)public}s"
+ "No media source with identifier %!{(MISSING)public}s"
+ "Received new media source identifier %!{(MISSING)public}s"
+ "Service %!{(MISSING)public}s received all values"
+ "Source %!{(MISSING)public}s has %!{(MISSING)public}ld media item(s)"
+ "Source has not received all values: %!{(MISSING)public}s"
+ "initWithTitles:artworkData:mediaSourceType:mediaSourceIdentifier:artworkToken:mediaItemImageToken:artworkType:multicast:"
+ "multicast"
- "Found media item with identifier %!s(MISSING)"
- "No media source with identifier %!s(MISSING)"
- "Received new media source identifier %!s(MISSING)"
- "Resizing SXM station logo to center on platter."
- "Reusing existing artwork data of length %!l(MISSING)d."
- "Service %!@(MISSING) received all values"
- "Source %!s(MISSING) has %!l(MISSING)d media item(s)"
- "Source has not received all values: %!s(MISSING)"
- "artworkData"
- "dataWithData:"
- "initWithTitles:artworkData:mediaSourceType:mediaSourceIdentifier:artworkToken:mediaItemImageToken:"

```

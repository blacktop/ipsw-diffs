## assetutil

> `/usr/bin/assetutil`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1007.0.0.0.0
+1008.0.0.0.0
   __TEXT.__text: 0xe8250
   __TEXT.__auth_stubs: 0x2710
-  __TEXT.__objc_stubs: 0xbb40
-  __TEXT.__objc_methlist: 0x72a0
+  __TEXT.__objc_stubs: 0xbb20
+  __TEXT.__objc_methlist: 0x7290
   __TEXT.__const: 0x74e18
   __TEXT.__gcc_except_tab: 0x1338
-  __TEXT.__objc_methname: 0x1147b
-  __TEXT.__objc_classname: 0x104d
-  __TEXT.__objc_methtype: 0x41d6
-  __TEXT.__cstring: 0x1538b
+  __TEXT.__objc_methname: 0x11478
+  __TEXT.__objc_classname: 0x1071
+  __TEXT.__objc_methtype: 0x41f1
+  __TEXT.__cstring: 0x153cb
   __TEXT.__oslogstring: 0x28
   __TEXT.__swift5_typeref: 0x8a
   __TEXT.__swift5_capture: 0x68

   __DATA_CONST.__got: 0x638
   __DATA_CONST.__auth_ptr: 0x100
   __DATA.__objc_const: 0xb6e8
-  __DATA.__objc_selrefs: 0x3cc0
+  __DATA.__objc_selrefs: 0x3cb8
   __DATA.__objc_ivar: 0x990
   __DATA.__objc_data: 0x24e0
   __DATA.__data: 0x810

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 3917
+  Functions: 3916
   Symbols:   823
   CStrings:  5828
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dkyZL5/Sources/CoreUI/Bom/Common/BOMBufferManager.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dkyZL5/Sources/CoreUI/Bom/Common/BOMFile.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dkyZL5/Sources/CoreUI/Bom/Common/BOMStack.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dkyZL5/Sources/CoreUI/Bom/Storage/BOMStorage.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dkyZL5/Sources/CoreUI/Bom/Storage/BOMStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dkyZL5/Sources/CoreUI/Bom/Storage/BOMTree.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dkyZL5/Sources/CoreUI/CoreTheme/CUICatalog.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dkyZL5/Sources/CoreUI/CoreTheme/ImageUtils/CUIDeepmap2Compression.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dkyZL5/Sources/CoreUI/CoreTheme/ImageUtils/CUIDeepmapCompression.m"
+ "@\"assetutilCUIVectorGlyphDrawAttachmentDataStore\""
+ "@\"assetutilCUIVectorGlyphDrawAttachmentDataStore\"16@0:8"
+ "@\"assetutilCUIVectorGlyphManagedPointArray\""
+ "CoreUI: Car file '%s' couldn't read swapped header block."
+ "T@\"assetutilCUIVectorGlyphManagedPointArray\",R,&,N,V_anchors"
+ "assetutilCUICatalogCSIGenerator"
+ "assetutilCUISingleNamedAssetMutableStorage"
+ "assetutilCUIVectorGlyphDrawAttachmentDataStore"
+ "assetutilCUIVectorGlyphManagedPointArray"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.e9BJyl/Sources/CoreUI/Bom/Common/BOMBufferManager.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.e9BJyl/Sources/CoreUI/Bom/Common/BOMFile.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.e9BJyl/Sources/CoreUI/Bom/Common/BOMStack.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.e9BJyl/Sources/CoreUI/Bom/Storage/BOMStorage.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.e9BJyl/Sources/CoreUI/Bom/Storage/BOMStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.e9BJyl/Sources/CoreUI/Bom/Storage/BOMTree.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.e9BJyl/Sources/CoreUI/CoreTheme/CUICatalog.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.e9BJyl/Sources/CoreUI/CoreTheme/ImageUtils/CUIDeepmap2Compression.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.e9BJyl/Sources/CoreUI/CoreTheme/ImageUtils/CUIDeepmapCompression.m"
- "@\"CUIVectorGlyphDrawAttachmentDataStore\""
- "@\"CUIVectorGlyphDrawAttachmentDataStore\"16@0:8"
- "@\"CUIVectorGlyphManagedPointArray\""
- "CUICatalogCSIGenerator"
- "CUISingleNamedAssetMutableStorage"
- "CUIVectorGlyphDrawAttachmentDataStore"
- "CUIVectorGlyphManagedPointArray"
- "T@\"CUIVectorGlyphManagedPointArray\",R,&,N,V_anchors"
- "_swapHeader"
```

## CoreVideo

> `/System/Library/Frameworks/CoreVideo.framework/CoreVideo`

```diff

-  __TEXT.__text: 0x6e464
+  __TEXT.__text: 0x6eeb8
   __TEXT.__const: 0x5ca8
-  __TEXT.__cstring: 0xba6c
+  __TEXT.__cstring: 0xc53c
   __TEXT.__oslogstring: 0x2e3
   __TEXT.__objc_databytes: 0x493
   __TEXT.__gcc_except_tab: 0x64

   __TEXT.__swift5_capture: 0x68
   __TEXT.__swift5_types2: 0x8
   __TEXT.__dof_CVPixelBu: 0x24a
-  __TEXT.__unwind_info: 0x1d18
+  __TEXT.__unwind_info: 0x1d70
   __TEXT.__eh_frame: 0x85c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __AUTH_CONST.__objc_dictobj: 0x192d0
   __AUTH_CONST.__objc_intobj: 0x2268
   __AUTH_CONST.__objc_arrayobj: 0x4878
-  __AUTH_CONST.__auth_got: 0xea0
+  __AUTH_CONST.__auth_got: 0xeb0
   __AUTH.__objc_dataobj: 0x9a8
   __AUTH.__objc_databytes: 0x330
   __AUTH.__data: 0x758

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 3621
-  Symbols:   11308
-  CStrings:  1385
+  Functions: 3631
+  Symbols:   11330
+  CStrings:  1420
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__dof_CVPixelBu : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_dataobj : content changed
~ __AUTH.__objc_databytes : content changed
~ __AUTH.__data : content changed
~ __AUTH.__thread_vars : content changed
~ __DATA.__data : content changed
Symbols:
+ _CFAllocatorGetTypeID
+ _CFSetApplyFunction
+ _CVArrayAppendSInt64Value
+ __ZL24allArrayElementsHaveTypePK9__CFArraym
+ __ZL28isCFNumberOrArrayOfCFNumbersPKv
+ __ZL29checkRequiredCompatibilityKeyPKvPv
+ __ZL30resolveKeyUsingLCMIntegerValuePK9__CFArrayP14__CFDictionaryPK10__CFString
+ __ZL30resolveKeyUsingMaxIntegerValuePK9__CFArrayP14__CFDictionaryPK10__CFString
+ __ZL33resolveKeyRequiringValueConsensusPK9__CFArrayP14__CFDictionaryPK10__CFStringmPKc
+ __ZL33setRequiredCompatibilityKeyToTruePKvPv
+ __ZL36resolveKeyUsingMergedDictionaryValuePK9__CFArrayP14__CFDictionaryPK10__CFString
+ __ZL36resolveKeyUsingORAcrossBooleanValuesPK9__CFArrayP14__CFDictionaryPK10__CFString
+ __ZL48addBooleanCompatibilityKeyToRequiredSetIfPresentPK14__CFDictionaryPK10__CFStringP7__CFSet
- __ZL19mergeCFDictionariesPKvS0_Pv
CStrings:
+ "CVPixelBufferCreateResolvedAttributesDictionary: conflict merging dictionary: key %@, values %@ and %@"
+ "Returning err %d because attributes is NULL"
+ "Returning err %d because attributes is not a CFArray"
+ "Returning err %d because bitsPerBlockRef is not a CFNumber"
+ "Returning err %d because could not allocate filteredPixelFormatTypesRef"
+ "Returning err %d because could not allocate oldIOSurfaceProperties"
+ "Returning err %d because could not allocate realTimeCacheModeArray"
+ "Returning err %d because could not allocate requiredCompatibility"
+ "Returning err %d because could not allocate result"
+ "Returning err %d because element is NULL"
+ "Returning err %d because element is not a CFDictionary"
+ "Returning err %d because key is not a CFString"
+ "Returning err %d because pixelFormatDescription is not a CFDictionary"
+ "Returning err %d because planeRef is not a CFDictionary"
+ "Returning err %d because resolvedDictionaryOut is NULL"
+ "Returning err %d because result is not a CFDictionary"
+ "Returning err %d because the resolved value for %@ is not a CFNumber"
+ "Returning err %d because the resolved value for kCVPixelBufferBytesPerRowAlignmentKey is not a CFNumber"
+ "Returning err %d because the value for %@ is not a CFBoolean"
+ "Returning err %d because the value for %@ is not a CFDictionary"
+ "Returning err %d because the value for %@ is not a CFNumber"
+ "Returning err %d because the value for %@ is not of the expected CFType"
+ "Returning err %d because the value for kCVPixelBufferBytesPerRowAlignmentKey is not a CFNumber"
+ "Returning err %d because the value for kCVPixelBufferCacheModeKey contains a non-CFNumber element"
+ "Returning err %d because the value for kCVPixelBufferCacheModeKey is not a CFArray"
+ "Returning err %d because the value for kCVPixelBufferExactBytesPerRowKey contains a non-CFNumber element"
+ "Returning err %d because the value for kCVPixelBufferExactBytesPerRowKey is not a CFNumber or a CFArray of CFNumbers"
+ "Returning err %d because the value for kCVPixelBufferIOSurfacePropertiesKey is not a CFDictionary"
+ "Returning err %d because the value for kCVPixelBufferPixelFormatTypeKey contains a non-CFNumber element"
+ "Returning err %d because the value for kCVPixelBufferPixelFormatTypeKey is not a CFArray"
+ "Returning err %d because the value for kCVPixelBufferPixelFormatTypeKey is not a CFNumber or a CFArray of CFNumbers"
+ "Returning err %d because the value for kCVPixelBufferPreferRealTimeCacheModeIfEveryoneDoesKey is not a CFBoolean"
+ "Returning err %d because the value for kIOSurfaceCacheMode is not a CFNumber"
+ "bytes per row alignment vs exact bytes per row mismatch"
+ "checkIOOrEXSurfaceAndCreatePixelBufferBacking returning err %d because planeHeight[planeIndex %u] %u is not equal to %u required by image height %u and verticalSubsampling %u"
+ "checkIOOrEXSurfaceAndCreatePixelBufferBacking returning err %d because planeWidth[planeIndex %u] %u is not equal to %u required by image width %u and horizontalSubsampling %u"
+ "exact height does not match supplied height"
+ "planar bytes per row alignment vs exact bytes per row mismatch"
+ "unmergeable attachment dictionary"
- "CVPixelBufferCreateResolvedAttributesDictionary: conflict merging IOSurfaceProperties: key %@, values %@ and %@"
- "bytes per row alignemnt vs exact bytes per row mismatch"
- "custom layout size mismatch"
- "planar bytes per row alignemnt vs exact bytes per row mismatch"

```

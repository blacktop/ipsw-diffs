## footprint

> `/usr/bin/footprint`

```diff

-240.40.2.0.0
-  __TEXT.__text: 0x17e64
-  __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__objc_stubs: 0x1de0
-  __TEXT.__objc_methlist: 0xd78
+253.100.1.0.0
+  __TEXT.__text: 0x186cc
+  __TEXT.__auth_stubs: 0xbe0
+  __TEXT.__objc_stubs: 0x1fc0
+  __TEXT.__objc_methlist: 0xdf0
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x1fc
-  __TEXT.__cstring: 0x2ccf
-  __TEXT.__objc_classname: 0x1d9
-  __TEXT.__objc_methname: 0x1f25
-  __TEXT.__objc_methtype: 0x6db
+  __TEXT.__cstring: 0x2d86
+  __TEXT.__objc_classname: 0x1f9
+  __TEXT.__objc_methname: 0x2133
+  __TEXT.__objc_methtype: 0x751
   __TEXT.__ustring: 0xd0
-  __TEXT.__unwind_info: 0x438
-  __DATA_CONST.__auth_got: 0x5f8
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0x15c8
-  __DATA_CONST.__cfstring: 0x1d20
+  __TEXT.__unwind_info: 0x454
+  __DATA_CONST.__auth_got: 0x600
+  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__const: 0x1650
+  __DATA_CONST.__cfstring: 0x1e00
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x170
+  __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x31b0
-  __DATA.__objc_selrefs: 0x810
-  __DATA.__objc_classrefs: 0x168
-  __DATA.__objc_superrefs: 0x98
-  __DATA.__objc_ivar: 0x264
+  __DATA.__objc_const: 0x3330
+  __DATA.__objc_selrefs: 0x890
+  __DATA.__objc_ivar: 0x274
   __DATA.__objc_data: 0x730
-  __DATA.__data: 0x1e8
-  __DATA.__bss: 0x4120
+  __DATA.__data: 0x248
+  __DATA.__bss: 0x4140
   __DATA.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication
   - /System/Library/PrivateFrameworks/Symbolication.framework/Symbolication
   - /System/Library/PrivateFrameworks/perfdata.framework/perfdata
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 386
-  Symbols:   262
-  CStrings:  1044
+  Functions: 399
+  Symbols:   265
+  CStrings:  1082
 
Symbols:
+ _OBJC_CLASS_$_IOSurfaceDebugDescription
+ __DefaultRuneLocale
+ ___maskrune
CStrings:
+ "\x03!!\x12"
+ "\nDue to errors, summary results may be incomplete or incorrect\n"
+ "\nErrors were encountered while examining the process. Results may be incomplete or incorrect.\n"
+ "           start                end  [object-id]     VRT     DRT%*s     CLN     RCL%*s   tag (detail)\n"
+ "        unmapped -         unmapped [%010llx]"
+ "      ----------         ---------- ------------   -----   -----%*s   -----   -----%*s   ------------\n"
+ "   %s%*s%*s\n"
+ "  '%@'"
+ "!datum2 || datum1.fp_isContainer == datum2.fp_isContainer"
+ "%16llx - %16llx [%010llx]"
+ "%4d"
+ "-[NSDictionary(FPAuxData) fp_mergeAuxDatum:withDatum:forceAggregate:]"
+ "@\"NSDictionary\"28@0:8Q16i24"
+ "@28@0:8Q16i24"
+ "@36@0:8i16Q20@28"
+ "B24@?0@\"IOSurfaceDebugDescription\"8@\"NSDictionary\"16"
+ "FPFootprintExtendedInfoProvider"
+ "Height"
+ "MALLOC metadata"
+ "Name"
+ "PixelFormat"
+ "SID: %#x  %ux%u (%s)"
+ "T@\"NSString\",&,N"
+ "T@\"NSString\",?,R,C"
+ "TI,R,N"
+ "Width"
+ "_allPIDsIOSurfaceDescriptions"
+ "_allPIDsIOSurfaceDescriptionsLock"
+ "_hasProcessViewForSingleTotalRegions"
+ "_isProcessViewForSingleTotalRegions"
+ "appendFormat:"
+ "extendedInfo"
+ "extendedInfoForRegionType:at:extendedInfoProvider:"
+ "fp_isContainer"
+ "fp_jsonRepresentation"
+ "fp_mergeAuxDatum:withDatum:forceAggregate:"
+ "fp_mergeWithData:"
+ "fp_mergeWithData:forceAggregate:"
+ "gatherData:extendedInfoProvider:"
+ "height"
+ "ioSurfaceExtendedInfoDetailsAtAddress:for:"
+ "numberWithUnsignedInt:"
+ "pixelFormat"
+ "predicateWithBlock:"
+ "setExtendedInfo:"
+ "surfaceDescriptions"
+ "surfaceID"
+ "unsignedIntValue"
+ "v28@0:8B16@20"
+ "virtualAddress"
+ "weakToStrongObjectsMapTable"
+ "width"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "\x02\x11!\x12"
- "\nDue to errors, summary results may be invalid\n"
- "\nErrors were encountered while examining the process. No results gathered.\n"
- "           start                end  [objectid]      VRT     DRT%*s     CLN     RCL%*s   tag (detail)\n"
- "        unmapped -         unmapped [%10llx]"
- "      ----------         ----------  ----------    -----   -----%*s   -----   -----%*s   ------------\n"
- "   %s%*s\n"
- "!datum2 || datum1.isContainer == datum2.isContainer"
- "%16llx - %16llx [%10llx]"
- "-[NSDictionary(FPAuxData) mergeAuxDatum:withDatum:forceAggregate:]"
- "MALLOC"
- "isContainer"
- "jsonRepresentation"
- "mergeAuxDatum:withDatum:forceAggregate:"
- "mergeWithData:"
- "mergeWithData:forceAggregate:"

```

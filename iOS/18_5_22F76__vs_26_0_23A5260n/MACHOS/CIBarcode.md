## CIBarcode

> `/System/Library/CoreImage/CIBarcode.cifilter/CIBarcode`

```diff

-1510.120.2.0.0
-  __TEXT.__text: 0xebb8
-  __TEXT.__auth_stubs: 0x470
-  __TEXT.__objc_stubs: 0xc80
-  __TEXT.__objc_methlist: 0x498
-  __TEXT.__cstring: 0x1493
-  __TEXT.__const: 0x5fd0
+1566.0.0.0.0
+  __TEXT.__text: 0xf500
+  __TEXT.__auth_stubs: 0x480
+  __TEXT.__objc_stubs: 0xda0
+  __TEXT.__objc_methlist: 0x560
+  __TEXT.__cstring: 0x20ba
+  __TEXT.__const: 0x5fe0
   __TEXT.__oslogstring: 0x77a
-  __TEXT.__objc_classname: 0x9c
-  __TEXT.__objc_methname: 0xb5c
-  __TEXT.__objc_methtype: 0x1af
-  __TEXT.__gcc_except_tab: 0x414
-  __TEXT.__unwind_info: 0x2f0
-  __DATA_CONST.__auth_got: 0x248
-  __DATA_CONST.__got: 0x170
+  __TEXT.__objc_classname: 0xb7
+  __TEXT.__objc_methname: 0xd7c
+  __TEXT.__objc_methtype: 0x1ba
+  __TEXT.__gcc_except_tab: 0x418
+  __TEXT.__unwind_info: 0x2f8
+  __DATA_CONST.__auth_got: 0x250
+  __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x490
-  __DATA_CONST.__cfstring: 0x1200
-  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__const: 0x4b0
+  __DATA_CONST.__cfstring: 0x1320
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__objc_intobj: 0x1f8
-  __DATA.__objc_const: 0x888
-  __DATA.__objc_selrefs: 0x3c0
-  __DATA.__objc_ivar: 0x60
-  __DATA.__objc_data: 0x230
+  __DATA_CONST.__objc_intobj: 0x240
+  __DATA_CONST.__objc_doubleobj: 0x40
+  __DATA.__objc_const: 0xa48
+  __DATA.__objc_selrefs: 0x460
+  __DATA.__objc_ivar: 0x78
+  __DATA.__objc_data: 0x280
   __DATA.__data: 0x18
   __DATA.__bss: 0x248
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 33513477-243E-312B-949D-7E7DA0149E89
-  Functions: 267
-  Symbols:   129
-  CStrings:  560
+  UUID: 1C96A8D4-48E9-3DC0-A56D-B98D0AA72A7F
+  Functions: 283
+  Symbols:   135
+  CStrings:  607
 
Symbols:
+ _OBJC_CLASS_$_CIColor
+ _OBJC_CLASS_$_CIKernel
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _kCIAttributeTypeColor
+ _kCIAttributeTypeScalar
+ _objc_retain_x28
CStrings:
+ "16.0"
+ "19"
+ "@\"CIColor\""
+ "CIRoundedQRCodeGenerator"
+ "T@\"CIColor\",&,N,VinputColor0"
+ "T@\"CIColor\",&,N,VinputColor1"
+ "T@\"NSNumber\",C,N,VinputCenterSpaceSize"
+ "T@\"NSNumber\",C,N,VinputRoundedData"
+ "T@\"NSNumber\",C,N,VinputRoundedMarkers"
+ "T@\"NSNumber\",C,N,VinputScale"
+ "applyWithExtent:roiCallback:arguments:"
+ "blackColor"
+ "boolValue"
+ "cachedKernelWithString:"
+ "extent"
+ "filterWithName:"
+ "float rrect (vec2 lo, vec2 hi, float radius, vec2 dc) \n { \n float side = min(hi.x-lo.x, hi.y-lo.y); \n radius = min(radius,side/3.0); \n vec2 v = max(min(dc - (lo + radius), 0.0), dc - (hi - radius)); \n return clamp((radius - length(v) + 0.5), 0.0, 1.0); \n } \n float k_Finder (float k, float scale, vec2 p, vec2 dc, vec2 o) \n { \n if (p.x < o.x || p.y < o.y || p.x > o.x + 9.0 || p.y > o.y + 9.0) \n return k; \n k = 1.0; \n vec2 lo = (o+vec2(1,1)) * scale + 1.0; \n vec2 hi = (o+vec2(8,8)) * scale - 1.0; \n k -= rrect(lo, hi, 1.5 * scale, dc); \n lo = (o+vec2(2,2)) * scale + 1.0; \n hi = (o+vec2(7,7)) * scale - 1.0; \n k += rrect(lo, hi, 0.75 * scale, dc); \n lo = (o+vec2(3,3)) * scale + 1.0; \n hi = (o+vec2(6,6)) * scale - 1.0; \n k -= rrect(lo, hi, 0.5 * scale, dc); \n return k; \n } \n float k_Align (float k, float scale, vec2 p, vec2 dc, vec2 o) \n { \n if (p.x < o.x || p.y < o.y || p.x > o.x + 5.0 || p.y > o.y + 5.0) \n return k; \n k = 1.0; \n vec2 lo = (o+vec2(0,0)) * scale + 1.0 + 0.2*scale; \n vec2 hi = (o+vec2(5,5)) * scale - 1.0 - 0.2*scale; \n k -= rrect(lo, hi, 1.25 * scale, dc); \n lo = (o+vec2(1,1)) * scale + 1.0; \n hi = (o+vec2(4,4)) * scale - 1.0; \n k += rrect(lo, hi, 0.5 * scale, dc); \n lo = (o+vec2(2,2)) * scale; \n hi = (o+vec2(3,3)) * scale; \n k -= rrect(lo, hi, 0.25 * scale, dc); \n return k; \n } \n kernel vec4 qrScaler (sampler image, float scale, float centerArea, float roundData, float roundMarker, __color c0, __color c1) { \n vec2 dc = destCoord(); \n vec2 dcSnapped = (floor(dc/scale)+0.5)*scale; \n vec2 ssize = samplerSize(image); \n vec2 p = floor(dc/scale)+0.5; \n vec4 c = sample(image, samplerTransform(image,p)); \n float k = c.r; \n if (roundData > 0.5) \n { \n float dist = length(dc-dcSnapped); \n float mixer = clamp(dist+1.0-scale*0.5,0.0,1.0); \n k = mix(k, 1.0, mixer); \n } \n if (roundMarker > 0.5) \n { \n k = k_Finder(k, scale, p, dc, vec2(0, 0)); \n k = k_Finder(k, scale, p, dc, vec2(0, ssize.y-9.0)); \n k = k_Finder(k, scale, p, dc, vec2(ssize.x-9.0, ssize.y-9.0)); \n } \n if (roundMarker > 1.5 && ssize.x>=46.0 && ssize.x<=73.0) \n { \n float Min = 5.0; \n float Max = (ssize.x-10.0); \n float Mid = (Min + Max) * 0.5; \n k = k_Align(k, scale, p, dc, vec2(Min, Mid)); \n k = k_Align(k, scale, p, dc, vec2(Mid, Min)); \n k = k_Align(k, scale, p, dc, vec2(Mid, Mid)); \n k = k_Align(k, scale, p, dc, vec2(Mid, Max)); \n k = k_Align(k, scale, p, dc, vec2(Max, Min)); \n k = k_Align(k, scale, p, dc, vec2(Max, Mid)); \n } \n if (centerArea > 0.0) \n { \n vec2 lo = floor(ssize*(0.5 - 0.5*centerArea)); \n vec2 hi = ceil(ssize*(0.5 + 0.5*centerArea)); \n if (hi.x - lo.x >= 7.0) \n { \n lo *= scale; \n hi *= scale; k = max(k, rrect(lo, hi, 0.5 * scale, dc)); \n lo += scale; \n hi -= scale; \n k -= rrect(lo, hi, 1.5 * scale, dc); \n } \n } \n if (roundMarker > 1.5 && ssize.x>=25.0 && ssize.x<=45.0) \n { \n float Min = 5.0; \n float Max = (ssize.x-10.0); \n k = k_Align(k, scale, p, dc, vec2(Max, Min)); \n } \n return mix(c1,c0,k) * c.a; \n } \n"
+ "inputCenterSpaceSize"
+ "inputColor0"
+ "inputColor1"
+ "inputRoundedData"
+ "inputRoundedMarkers"
+ "inputScale"
+ "numberWithFloat:"
+ "setInputCenterSpaceSize:"
+ "setInputColor0:"
+ "setInputColor1:"
+ "setInputRoundedData:"
+ "setInputRoundedMarkers:"
+ "setInputScale:"
+ "whiteColor"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}44@?0i8{CGRect={CGPoint=dd}{CGSize=dd}}12"

```

## CoreGPSTest.dylib

> `/System/Library/PrivateFrameworks/CoreGPSTest.framework/CoreGPSTest.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-365.0.9.0.1
-  __TEXT.__text: 0x65e60
+367.0.1.0.0
+  __TEXT.__text: 0x65da0
   __TEXT.__init_offsets: 0xc
   __TEXT.__objc_methlist: 0x164
   __TEXT.__const: 0x6570
-  __TEXT.__gcc_except_tab: 0x3988
-  __TEXT.__oslogstring: 0xaa72
+  __TEXT.__gcc_except_tab: 0x3974
+  __TEXT.__oslogstring: 0xaa6e
   __TEXT.__constg_swiftt: 0x408
   __TEXT.__swift5_typeref: 0x18a
   __TEXT.__swift5_reflstr: 0x8f

   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0xbb8
+  __AUTH_CONST.__auth_got: 0xbb0
   __AUTH.__objc_data: 0x170
   __AUTH.__data: 0x748
   __DATA.__objc_ivar: 0x8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 2684
-  Symbols:   4382
+  Symbols:   4380
   CStrings:  1368
 
Symbols:
+ __ZN11NmeaLogging13NmeaExtractor4feedEPKhm
- __ZN11NmeaLogging13NmeaExtractor4feedERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEcm
- __ZNKSt3__114default_deleteIN11NmeaLogging13NmeaExtractorEEclB9fqe220106EPS2_
Functions:
~ __ZN21GnssIndicationHandler4sendERKN4gnss15MeasurementDataE : 996 -> 988
~ __ZN12VendorLoggerC2ERKNS_6ConfigE : 2156 -> 2072
~ __ZN12VendorLoggerD2Ev : 476 -> 460
~ __ZN12VendorLogger7restartEv : 68 -> 28
~ ____ZN12VendorLogger3logEONSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE_block_invoke : 152 -> 120
~ __ZN11NmeaLogging13NmeaExtractor4feedERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE -> __ZN11NmeaLogging13NmeaExtractor4feedEPKhm : 344 -> 316
~ __ZN4cCLP8LogEntry11PrivateData6cpbHalERKNS1_6SvInfoERKNSt3__16vectorIhNS5_9allocatorIhEEEERN4gnss6SvInfoE : 1112 -> 1120
~ __ZN4cCLP8LogEntry11PrivateData6cpbHalERKN4gnss6SvInfoERNS1_6SvInfoERNSt3__16vectorIhNS8_9allocatorIhEEEE : 228 -> 236
CStrings:
+ "#version,CoreGPS-367.0.1,machContSec,%{public}.3f,BuildTime,{Sep  9 2026,20:53:27}"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "#version,CoreGPS-365.0.9.0.1,machContSec,%{public}.3f,BuildTime,{Aug 13 2026,21:42:35}"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
```

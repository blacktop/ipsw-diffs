## CoreGPSTest.dylib

> `/System/Library/PrivateFrameworks/CoreGPSTest.framework/CoreGPSTest.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__oslogstring`
- `__TEXT.__cstring`

```diff

-367.0.2.0.0
-  __TEXT.__text: 0x65e0c
+369.0.1.0.0
+  __TEXT.__text: 0x663f0
   __TEXT.__init_offsets: 0xc
   __TEXT.__objc_methlist: 0x164
-  __TEXT.__const: 0x6570
-  __TEXT.__gcc_except_tab: 0x3974
+  __TEXT.__const: 0x6580
+  __TEXT.__gcc_except_tab: 0x398c
   __TEXT.__oslogstring: 0xaa81
   __TEXT.__constg_swiftt: 0x408
   __TEXT.__swift5_typeref: 0x18a

   __TEXT.__swift5_types: 0x30
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x2bb0
+  __TEXT.__unwind_info: 0x2bf8
   __TEXT.__eh_frame: 0x650
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __AUTH.__data: 0x748
   __DATA.__objc_ivar: 0x8
   __DATA.__data: 0xd0
-  __DATA.__common: 0x9ee28
+  __DATA.__common: 0x9e3a8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2684
-  Symbols:   4318
+  Functions: 2692
+  Symbols:   4326
   CStrings:  1369
 
Symbols:
+ __ZN4cCLP8LogEntry11PrivateData6cpbHalERKN4gnss13ReceiverClockERNS1_5ClockERNSt3__16vectorIhNS8_9allocatorIhEEEE
+ __ZN4cCLP8LogEntry11PrivateData6cpbHalERKN4gnss18ReceiverClockModelERNS1_18ReceiverClockModelERNSt3__16vectorIhNS8_9allocatorIhEEEE
+ __ZN4cCLP8LogEntry11PrivateData6cpbHalERKN4gnss18TimeConversionInfoERNS1_18TimeConversionInfoERNSt3__16vectorIhNS8_9allocatorIhEEEE
+ __ZN4cCLP8LogEntry11PrivateData6cpbHalERKNS1_18ReceiverClockModelERKNSt3__16vectorIhNS5_9allocatorIhEEEERN4gnss18ReceiverClockModelE
+ __ZN4cCLP8LogEntry11PrivateData6cpbHalERKNS1_18TimeConversionInfoERKNSt3__16vectorIhNS5_9allocatorIhEEEERN4gnss18TimeConversionInfoE
+ __ZN4cCLP8LogEntry11PrivateData6cpbHalERKNS1_5ClockERKNSt3__16vectorIhNS5_9allocatorIhEEEERN4gnss13ReceiverClockE
+ __ZN4gnss20MeasurementExtensionD2Ev
+ __ZN6cproto4gnss11cpbOptionalILb0EN4gnss11GpsTimeInfoEN4cCLP8LogEntry11PrivateData11GpsTimeInfoEEEbRKT0_RNS0_9toptionalIT1_EERNSt3__16vectorIhNSF_9allocatorIhEEEE
+ __ZN6cproto4gnss11cpbOptionalILb0EN4gnss13NavicTimeInfoEN4cCLP8LogEntry11PrivateData13NavicTimeInfoEEEbRKT0_RNS0_9toptionalIT1_EERNSt3__16vectorIhNSF_9allocatorIhEEEE
+ __ZN6cproto4gnss11cpbOptionalILb0EN4gnss14BeidouTimeInfoEN4cCLP8LogEntry11PrivateData14BeidouTimeInfoEEEbRKT0_RNS0_9toptionalIT1_EERNSt3__16vectorIhNSF_9allocatorIhEEEE
+ __ZN6cproto4gnss11cpbOptionalILb0EN4gnss15GalileoTimeInfoEN4cCLP8LogEntry11PrivateData15GalileoTimeInfoEEEbRKT0_RNS0_9toptionalIT1_EERNSt3__16vectorIhNSF_9allocatorIhEEEE
+ __ZN6cproto4gnss11cpbOptionalILb0EN4gnss15GlonassTimeInfoEN4cCLP8LogEntry11PrivateData15GlonassTimeInfoEEEbRKT0_RNS0_9toptionalIT1_EERNSt3__16vectorIhNSF_9allocatorIhEEEE
+ __ZN6cproto4gnss11cpbOptionalILb0EffEEbRKNSt3__18optionalIT0_EERNS0_9toptionalIT1_EERNS2_6vectorIhNS2_9allocatorIhEEEE
+ __ZN6cproto4gnss11cpbOptionalILb1EN4gnss15PolynomialOrbitEN4cCLP8LogEntry11PrivateData15PolynomialOrbitEEEbRKT0_RNS0_9toptionalIT1_EERNSt3__16vectorIhNSF_9allocatorIhEEEE
- __ZN4cCLP8LogEntry11PrivateData6cpbHalERKN4gnss13ReceiverClockERNS1_5ClockE
- __ZN4cCLP8LogEntry11PrivateData6cpbHalERKN4gnss18ReceiverClockModelERNS1_18ReceiverClockModelE
- __ZN4cCLP8LogEntry11PrivateData6cpbHalERKN4gnss18TimeConversionInfoERNS1_18TimeConversionInfoE
- __ZN4cCLP8LogEntry11PrivateData6cpbHalERKNS1_18ReceiverClockModelERN4gnss18ReceiverClockModelE
- __ZN4cCLP8LogEntry11PrivateData6cpbHalERKNS1_18TimeConversionInfoERN4gnss18TimeConversionInfoE
- __ZN4cCLP8LogEntry11PrivateData6cpbHalERKNS1_5ClockERN4gnss13ReceiverClockE
CStrings:
+ "#version,CoreGPS-369.0.1,machContSec,%{public}.3f,BuildTime,{Oct 24 2026,01:38:14}"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "#version,CoreGPS-367.0.2,machContSec,%{public}.3f,BuildTime,{Oct 13 2026,21:11:12}"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
```

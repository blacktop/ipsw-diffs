## IOKit

> `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`

```diff

-100065.80.2.0.0
-  __TEXT.__text: 0x9ddb0
-  __TEXT.__auth_stubs: 0x1fb0
+100076.102.2.0.0
+  __TEXT.__text: 0x9e8b8
+  __TEXT.__auth_stubs: 0x2020
   __TEXT.__objc_methlist: 0x14c
-  __TEXT.__oslogstring: 0x4818
-  __TEXT.__cstring: 0xb31d
+  __TEXT.__oslogstring: 0x48d4
+  __TEXT.__cstring: 0xb3fc
   __TEXT.__const: 0xea80
-  __TEXT.__unwind_info: 0x1e64
+  __TEXT.__unwind_info: 0x1e74
   __TEXT.__objc_classname: 0x58
   __TEXT.__objc_methname: 0xa3
   __TEXT.__objc_methtype: 0x1945
   __TEXT.__objc_stubs: 0x60
-  __DATA_CONST.__got: 0x1a0
+  __DATA_CONST.__got: 0x1a8
   __DATA_CONST.__const: 0x26a8
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x310
   __DATA_CONST.__objc_selrefs: 0x40
+  __DATA_CONST.__objc_classrefs: 0x38
+  __DATA_CONST.__objc_superrefs: 0x38
   __AUTH_CONST.__const: 0x1bb8
   __AUTH_CONST.__objc_const: 0x1f8
-  __AUTH_CONST.__cfstring: 0x6f00
+  __AUTH_CONST.__cfstring: 0x6fa0
   __AUTH_CONST.__auth_ptr: 0x50
-  __AUTH_CONST.__auth_got: 0xfe0
+  __AUTH_CONST.__auth_got: 0x1018
   __AUTH.__objc_data: 0x190
   __AUTH.__data: 0xa0
-  __DATA.__objc_classrefs: 0x38
-  __DATA.__objc_superrefs: 0x38
   __DATA.__objc_ivar: 0x1c
-  __DATA.__data: 0x888
+  __DATA.__data: 0x880
   __DATA.__bss: 0x228
   __DATA.__common: 0x100
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__data: 0xa8
+  __DATA_DIRTY.__data: 0xb0
   __DATA_DIRTY.__bss: 0x1c8
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3613
-  Symbols:   6049
-  CStrings:  2416
+  Functions: 3621
+  Symbols:   6063
+  CStrings:  2433
 
Symbols:
+ _CFBundleGetMainBundle
+ _CFCalendarCreateWithIdentifier
+ _CFDateFormatterCreateISO8601Formatter
+ _CFDateFormatterCreateStringWithDate
+ _CFStringCreateMutableCopy
+ _CFStringDelete
+ _IOAVServiceGetFRLCharacterErrorCounts
+ _IOAVServiceGetFRLLinkData
+ _IOAVServiceGetFRLMaxRate
+ _IOAVServiceGetFRLMinRate
+ _IOAVServiceRetrainFRL
+ _IOAVServiceSetFRLMaxRate
+ _IOAVServiceSetFRLMinRate
+ _IOAVServiceSetFRLRecovery
+ _IOPSGetYearAndWeekOfManufactureFromBatterySerial
+ __IOHIDEventDebugInfo
+ ___block_descriptor_tmp.161
+ ___block_descriptor_tmp.181
+ ___block_descriptor_tmp.192
+ ___block_descriptor_tmp.193
+ ___block_descriptor_tmp.226
+ ___block_descriptor_tmp.268
+ ___block_descriptor_tmp.270
+ _kCFGregorianCalendar
+ _strtoull
- ___block_descriptor_tmp.178
- ___block_descriptor_tmp.179
- ___block_descriptor_tmp.189
- ___block_descriptor_tmp.190
- ___block_descriptor_tmp.223
- ___block_descriptor_tmp.264
- ___block_descriptor_tmp.265
- _processAssertionUpdateActivity.cold.7
- _processAssertionUpdateActivity.cold.8
CStrings:
+ "%-25.25s %f\n"
+ "%s: Filtered event type:%d sender:%#llx eventInfo:(%@)"
+ "Begin"
+ "Bottom Button M1:"
+ "Bottom Button M2:"
+ "Bottom Button M3:"
+ "Bottom Button M4:"
+ "Cancelled"
+ "Changed"
+ "Copy Event filtered type:%d sender:0x%llx eventInfo:(%@) service filter:%@"
+ "DoubleSqueeze"
+ "Ended"
+ "Event filtered type:%d sender:0x%llx eventInfo:(%@) service filter:%@"
+ "Event filtered type:%d service:0x%llx eventInfo:(%@) session filter:%@"
+ "Extra Button L4:"
+ "Extra Button R4:"
+ "Length"
+ "LongSqueeze"
+ "MayBegin"
+ "OSKEXT_BUILD_DATE 20:54:45 Feb 16 2024"
+ "Powerd has requested active assertions update"
+ "Squeeze"
+ "buttonState: %d"
+ "keyboardPress: %d"
+ "powerd returned assertion id 0x%x for async id 0x%x \n"
+ "processCurrentActiveAssertions: No gAssertionConnection"
+ "vendorUsagePage: %d vendorUsage:%d dataLength:%d"
- "%s: Filtered event type:%d sender:0x%llx"
- "Copy Event filtered type:%d sender:0x%llx service filter:%@"
- "Event filtered type:%d sender:0x%llx service filter:%@"
- "No assertion activity to update"
- "OSKEXT_BUILD_DATE 18:02:28 Dec 20 2023"
- "Phase: Begin"
- "Phase: Cancelled"
- "Phase: Ended"
- "Phase: MayBegin"
- "powerd returned assertion id 0x%x for async id %@\n"

```

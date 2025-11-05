## iCalendar

> `/System/Library/PrivateFrameworks/iCalendar.framework/Versions/A/iCalendar`

```diff

 1167.0.0.0.0
-  __TEXT.__text: 0x2e1f0
+  __TEXT.__text: 0x2e2f4
   __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x36f0
+  __TEXT.__objc_methlist: 0x3914
   __TEXT.__oslogstring: 0x4c9
   __TEXT.__const: 0x490
-  __TEXT.__cstring: 0x2a11
+  __TEXT.__cstring: 0x2a0f
   __TEXT.__gcc_except_tab: 0x214
-  __TEXT.__unwind_info: 0xbb8
+  __TEXT.__unwind_info: 0xbd0
   __TEXT.__objc_classname: 0x69b
   __TEXT.__objc_methname: 0x5aa2
   __TEXT.__objc_methtype: 0x8b5

   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f40
+  __DATA_CONST.__objc_selrefs: 0x1fc0
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0xb0
   __AUTH_CONST.__auth_got: 0x318
   __AUTH_CONST.__const: 0x390
   __AUTH_CONST.__cfstring: 0x5080
-  __AUTH_CONST.__objc_const: 0x60b8
+  __AUTH_CONST.__objc_const: 0x5cf0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x640
   __DATA.__objc_ivar: 0x1dc

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 10BD5FDD-18C7-3FBF-BDB8-0E3D044EA58D
-  Functions: 1169
-  Symbols:   3066
-  CStrings:  2835
+  UUID: 85A028C2-9E4E-37BE-8476-7E91D67D2FB0
+  Functions: 1182
+  Symbols:   3086
+  CStrings:  2834
 
Symbols:
+ +[ICSLogger sharedInstance].cold.1
+ +[ICSProperty valueAndParameterClasses].cold.1
+ +[ICSTimeZone(Internal) quickTimeZoneNames].cold.1
+ +[ICSTimeZone(TimeZoneGeneration) _isTimeZone:pseudoDSTForDate:].cold.1
+ +[ICSTimeZoneTranslator timeZoneNameForNonstandardTimeZone:].cold.1
+ -[ICSComponent propertiesToExcludeForChecksum].cold.1
+ -[ICSProperty(ICSWriter) _ICSStringWithOptions:appendingToString:additionalParameters:].cold.1
+ -[ICSPushbackStream peek].cold.1
+ -[ICSPushbackStream pushBack:].cold.1
+ -[ICSPushbackStream pushBack:].cold.2
+ -[ICSRecurrenceRule initWithCoder:].cold.1
+ -[ICSUserAddress sanitizeAddressString:].cold.1
+ -[ICSZStringWriter _appendBytes:length:andFlush:].cold.1
+ -[NSMutableString(ICSWriter) controlCharacterSet].cold.1
+ -[NSString(VCSUtilities) VCS_isPhoneNumber].cold.1
+ ICSDefaultPRODID.cold.1
+ ICSRedactBytes.cold.1
+ VCSLogHandle.cold.1
+ logHandle.cold.1
+ symbolicColorForLegacyRGB.cold.1
- _OUTLINED_FUNCTION_3
CStrings:
- "0"

```

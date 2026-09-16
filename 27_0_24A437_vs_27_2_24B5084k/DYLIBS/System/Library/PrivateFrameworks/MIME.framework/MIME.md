## MIME

> `/System/Library/PrivateFrameworks/MIME.framework/MIME`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-3901.100.1.2.14
-  __TEXT.__text: 0x3308c
+3901.200.34.0.0
+  __TEXT.__text: 0x331a8
   __TEXT.__objc_methlist: 0x321c
-  __TEXT.__gcc_except_tab: 0x41b4
-  __TEXT.__const: 0x7a5
+  __TEXT.__gcc_except_tab: 0x41c8
+  __TEXT.__const: 0x790
   __TEXT.__cstring: 0x2a2a
-  __TEXT.__oslogstring: 0x1213
+  __TEXT.__oslogstring: 0x1244
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1ce0
+  __TEXT.__unwind_info: 0x1ce8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA.__data: 0x710
   __DATA_DIRTY.__objc_data: 0xe10
   __DATA_DIRTY.__data: 0xf0
-  __DATA_DIRTY.__common: 0x18
   __DATA_DIRTY.__bss: 0xf9
+  __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1214
-  Symbols:   3206
-  CStrings:  651
+  Functions: 1216
+  Symbols:   3208
+  CStrings:  652
 
Symbols:
+ -[MFMessageStore flushAllCaches]
+ _OUTLINED_FUNCTION_4
+ __OBJC_$_CATEGORY_NSData_$_MimeDataEncoding
+ __OBJC_$_CATEGORY_NSString_$_MimeCharsetSupport
+ __OBJC_$_CLASS_METHODS_NSString(MimeCharsetSupport|MimeHeaderEncoding|NSEmailAddressString|MFStringTransform|MFStringUtils)
+ __OBJC_$_INSTANCE_METHODS_MFMimePart(DecodeApplication|DecodeMultipart|MessageSupport|IMAPSupport|DecodingSupport)
+ __OBJC_$_INSTANCE_METHODS_NSData(MimeDataEncoding|NSDataExtensions|NSDataUtils|MFUUDecoder)
+ __OBJC_$_INSTANCE_METHODS_NSString(MimeCharsetSupport|MimeHeaderEncoding|NSEmailAddressString|MFStringTransform|MFStringUtils)
+ _kMaxNumberOfRecursiveSubParts
+ _objc_msgSend$flushAllCaches
- -[MFMessageStore _flushAllCaches]
- __OBJC_$_CATEGORY_NSData_$_NSDataExtensions
- __OBJC_$_CATEGORY_NSString_$_NSEmailAddressString
- __OBJC_$_CLASS_METHODS_NSString(NSEmailAddressString|MFStringTransform|MFStringUtils|MimeCharsetSupport|MimeHeaderEncoding)
- __OBJC_$_INSTANCE_METHODS_MFMimePart(MessageSupport|IMAPSupport|DecodingSupport|DecodeApplication|DecodeMultipart)
- __OBJC_$_INSTANCE_METHODS_NSData(NSDataExtensions|MimeDataEncoding|NSDataUtils|MFUUDecoder)
- __OBJC_$_INSTANCE_METHODS_NSString(NSEmailAddressString|MFStringTransform|MFStringUtils|MimeCharsetSupport|MimeHeaderEncoding)
- _objc_msgSend$_flushAllCaches
CStrings:
+ "<%@: %p> %@\n"
+ "Reached the maximum MIME part parsing depth: %lu"
- "<%@: %p> %s\n"
```

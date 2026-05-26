## SESShared

> `/System/Library/PrivateFrameworks/SESShared.framework/SESShared`

```diff

-65.3.1.0.0
-  __TEXT.__text: 0xea1c
-  __TEXT.__auth_stubs: 0x7d0
+66.4.0.0.0
+  __TEXT.__text: 0xec34
+  __TEXT.__auth_stubs: 0x800
   __TEXT.__objc_methlist: 0x7bc
   __TEXT.__const: 0xc38
   __TEXT.__cstring: 0x1750

   __TEXT.__unwind_info: 0x378
   __TEXT.__eh_frame: 0xb8
   __TEXT.__objc_classname: 0xf9
-  __TEXT.__objc_methname: 0x11df
+  __TEXT.__objc_methname: 0x1259
   __TEXT.__objc_methtype: 0x3f7
-  __TEXT.__objc_stubs: 0xcc0
+  __TEXT.__objc_stubs: 0xd00
   __DATA_CONST.__got: 0x170
   __DATA_CONST.__const: 0x8f0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x628
+  __DATA_CONST.__objc_selrefs: 0x620
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x3f8
+  __AUTH_CONST.__auth_got: 0x410
   __AUTH_CONST.__const: 0x1f8
   __AUTH_CONST.__cfstring: 0x2460
   __AUTH_CONST.__objc_const: 0xbb0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 7AB48F19-037C-3ADC-A57F-4AEA8C4FAEA0
-  Functions: 290
-  Symbols:   1148
-  CStrings:  968
+  UUID: 88A721F7-55A7-3E76-BC93-6AE9ED876C97
+  Functions: 296
+  Symbols:   1150
+  CStrings:  967
 
Symbols:
+ +[NSData(DERItem) ses_dataWithDERItem:]
+ +[NSData(HexString) ses_dataWithHexString:]
+ +[NSData(Integer) ses_withU16BE:]
+ +[NSData(Random) ses_randomData:]
+ +[NSString(AsciiData) ses_stringWithAsciiData:]
+ -[NSArray(Functional) ses_allSatisfy:]
+ -[NSArray(Functional) ses_filter:]
+ -[NSArray(Functional) ses_filterMap:]
+ -[NSArray(Functional) ses_find:]
+ -[NSArray(Random) ses_randomElement]
+ -[NSData(Base64) ses_base64]
+ -[NSData(DERItem) ses_DERItem]
+ -[NSData(DERItem) ses_isEqualToDERItem:]
+ -[NSData(HexString) ses_asHexString]
+ -[NSData(Integer) ses_s32BE:]
+ -[NSData(Integer) ses_u16BE:]
+ -[NSData(Integer) ses_u16LE:]
+ -[NSData(Integer) ses_u32BE:]
+ -[NSData(Integer) ses_u32LE:]
+ -[NSData(Integer) ses_u64BE:]
+ -[NSData(Integer) ses_u64LE:]
+ -[NSData(Integer) ses_u8:]
+ -[NSMutableArray(queue) ses_popFirst]
+ -[NSMutableArray(queue) ses_pushLast:]
+ -[NSMutableData(Append) ses_appendU16BE:]
+ -[NSMutableData(Append) ses_appendU16LE:]
+ -[NSMutableData(Append) ses_appendU32BE:]
+ -[NSMutableData(Append) ses_appendU32LE:]
+ -[NSMutableData(Append) ses_appendU64BE:]
+ -[NSMutableData(Append) ses_appendU64LE:]
+ -[NSMutableData(Append) ses_appendU8:]
+ -[NSSet(Functional) ses_allSatisfy:]
+ -[NSSet(Functional) ses_contains:]
+ -[NSSet(Functional) ses_filter:]
+ -[NSSet(Functional) ses_filterMap:]
+ -[NSSet(Functional) ses_find:]
+ -[NSString(AsciiData) ses_asAsciiData]
+ -[NSString(HexString) ses_hexStringAsData]
+ _objc_msgSend$ses_DERItem
+ _objc_msgSend$ses_asAsciiData
+ _objc_msgSend$ses_asHexString
+ _objc_msgSend$ses_base64
+ _objc_msgSend$ses_dataWithDERItem:
+ _objc_msgSend$ses_dataWithHexString:
+ _objc_msgSend$ses_hexStringAsData
- +[NSData(DERItem) dataWithDERItem:]
- +[NSData(HexString) dataWithHexString:]
- +[NSData(Integer) withU16BE:]
- +[NSData(Random) randomData:]
- +[NSString(AsciiData) stringWithAsciiData:]
- -[NSArray(Functional) allSatisfy:]
- -[NSArray(Functional) filter:]
- -[NSArray(Functional) filterMap:]
- -[NSArray(Functional) find:]
- -[NSArray(Random) randomElement]
- -[NSData(Base64) base64]
- -[NSData(DERItem) DERItem]
- -[NSData(DERItem) isEqualToDERItem:]
- -[NSData(HexString) asHexString]
- -[NSData(Integer) s32BE:]
- -[NSData(Integer) u16BE:]
- -[NSData(Integer) u16LE:]
- -[NSData(Integer) u32BE:]
- -[NSData(Integer) u32LE:]
- -[NSData(Integer) u64BE:]
- -[NSData(Integer) u64LE:]
- -[NSData(Integer) u8:]
- -[NSMutableArray(queue) popFirst]
- -[NSMutableArray(queue) pushLast:]
- -[NSMutableData(Append) appendU16BE:]
- -[NSMutableData(Append) appendU16LE:]
- -[NSMutableData(Append) appendU32BE:]
- -[NSMutableData(Append) appendU32LE:]
- -[NSMutableData(Append) appendU64BE:]
- -[NSMutableData(Append) appendU64LE:]
- -[NSMutableData(Append) appendU8:]
- -[NSSet(Functional) allSatisfy:]
- -[NSSet(Functional) contains:]
- -[NSSet(Functional) filter:]
- -[NSSet(Functional) filterMap:]
- -[NSSet(Functional) find:]
- -[NSString(AsciiData) asAsciiData]
- -[NSString(HexString) hexStringAsData]
- _objc_msgSend$DERItem
- _objc_msgSend$asHexString
- _objc_msgSend$base64
- _objc_msgSend$dataWithDERItem:
- _objc_msgSend$dataWithHexString:
CStrings:
+ "ses_DERItem"
+ "ses_allSatisfy:"
+ "ses_appendU16BE:"
+ "ses_appendU16LE:"
+ "ses_appendU32BE:"
+ "ses_appendU32LE:"
+ "ses_appendU64BE:"
+ "ses_appendU64LE:"
+ "ses_appendU8:"
+ "ses_asAsciiData"
+ "ses_asHexString"
+ "ses_base64"
+ "ses_dataWithDERItem:"
+ "ses_dataWithHexString:"
+ "ses_filter:"
+ "ses_filterMap:"
+ "ses_find:"
+ "ses_hexStringAsData"
+ "ses_isEqualToDERItem:"
+ "ses_popFirst"
+ "ses_pushLast:"
+ "ses_randomData:"
+ "ses_randomElement"
+ "ses_s32BE:"
+ "ses_stringWithAsciiData:"
+ "ses_u16BE:"
+ "ses_u16LE:"
+ "ses_u32BE:"
+ "ses_u32LE:"
+ "ses_u64BE:"
+ "ses_u64LE:"
+ "ses_u8:"
+ "ses_withU16BE:"
- "allSatisfy:"
- "appendU16BE:"
- "appendU16LE:"
- "appendU32BE:"
- "appendU32LE:"
- "appendU64BE:"
- "appendU64LE:"
- "appendU8:"
- "asAsciiData"
- "asHexString"
- "base64"
- "contains:"
- "dataWithDERItem:"
- "dataWithHexString:"
- "filter:"
- "filterMap:"
- "find:"
- "hexStringAsData"
- "isEqualToDERItem:"
- "popFirst"
- "pushLast:"
- "randomData:"
- "randomElement"
- "s32BE:"
- "stringWithAsciiData:"
- "u16BE:"
- "u16LE:"
- "u32BE:"
- "u32LE:"
- "u64BE:"
- "u64LE:"
- "u8:"
- "withU16BE:"

```

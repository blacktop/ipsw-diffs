## AAAFoundation

> `/System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation`

```diff

-83.0.0.0.0
-  __TEXT.__text: 0xefdc
+85.0.0.0.0
+  __TEXT.__text: 0xf56c
   __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_methlist: 0x16ec
+  __TEXT.__objc_methlist: 0x1774
   __TEXT.__const: 0xc0
   __TEXT.__oslogstring: 0xa14
-  __TEXT.__cstring: 0xe37
+  __TEXT.__cstring: 0xe4e
   __TEXT.__gcc_except_tab: 0x260
   __TEXT.__dlopen_cstrs: 0xac
-  __TEXT.__unwind_info: 0x560
-  __TEXT.__objc_classname: 0x2b4
-  __TEXT.__objc_methname: 0x36a1
-  __TEXT.__objc_methtype: 0x7c9
-  __TEXT.__objc_stubs: 0x26a0
-  __DATA_CONST.__got: 0x328
+  __TEXT.__unwind_info: 0x578
+  __TEXT.__objc_classname: 0x304
+  __TEXT.__objc_methname: 0x378f
+  __TEXT.__objc_methtype: 0x7d2
+  __TEXT.__objc_stubs: 0x2740
+  __DATA_CONST.__got: 0x330
   __DATA_CONST.__const: 0x928
-  __DATA_CONST.__objc_classlist: 0xc8
+  __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x48
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfc0
+  __DATA_CONST.__objc_selrefs: 0xff8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_superrefs: 0x68
   __AUTH_CONST.__auth_got: 0x478
   __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0xea0
-  __AUTH_CONST.__objc_const: 0x3178
+  __AUTH_CONST.__cfstring: 0xee0
+  __AUTH_CONST.__objc_const: 0x3658
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x174
-  __DATA.__data: 0x368
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x17c
+  __DATA.__data: 0x3c8
   __DATA.__bss: 0xc8
   __DATA_DIRTY.__objc_data: 0x730
   __DATA_DIRTY.__bss: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F447F889-D47E-3067-90E3-18B86681DB27
-  Functions: 549
-  Symbols:   2211
-  CStrings:  1167
+  UUID: E9D2923C-9774-3786-B3D7-172DDFF8FB89
+  Functions: 557
+  Symbols:   2256
+  CStrings:  1186
 
Symbols:
+ +[AAFResponseBodyRedactor redactedCopyForObject:forKeys:]
+ +[AAFResponseBodyRedactor redactedCopyForResponse:forKeys:]
+ -[AAFPrivacySensitiveDictionaryLog .cxx_destruct]
+ -[AAFPrivacySensitiveDictionaryLog description]
+ -[AAFPrivacySensitiveDictionaryLog initWithDictionary:forKeys:]
+ -[AAFPrivacySensitiveDictionaryLog keysToRedact]
+ -[AAFPrivacySensitiveDictionaryLog redactedDescription]
+ -[AAFPrivacySensitiveDictionaryLog response]
+ _OBJC_CLASS_$_AAFPrivacySensitiveDictionaryLog
+ _OBJC_CLASS_$_AAFResponseBodyRedactor
+ _OBJC_IVAR_$_AAFPrivacySensitiveDictionaryLog._keysToRedact
+ _OBJC_IVAR_$_AAFPrivacySensitiveDictionaryLog._response
+ _OBJC_METACLASS_$_AAFPrivacySensitiveDictionaryLog
+ _OBJC_METACLASS_$_AAFResponseBodyRedactor
+ __OBJC_$_CLASS_METHODS_AAFResponseBodyRedactor
+ __OBJC_$_INSTANCE_METHODS_AAFPrivacySensitiveDictionaryLog
+ __OBJC_$_INSTANCE_VARIABLES_AAFPrivacySensitiveDictionaryLog
+ __OBJC_$_PROP_LIST_AAFPrivacySensitiveDictionaryLog
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AAFPrivacySensitiveLog
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AAFPrivacySensitiveLog
+ __OBJC_$_PROTOCOL_REFS_AAFPrivacySensitiveLog
+ __OBJC_CLASS_PROTOCOLS_$_AAFPrivacySensitiveDictionaryLog
+ __OBJC_CLASS_RO_$_AAFPrivacySensitiveDictionaryLog
+ __OBJC_CLASS_RO_$_AAFResponseBodyRedactor
+ __OBJC_LABEL_PROTOCOL_$_AAFPrivacySensitiveLog
+ __OBJC_METACLASS_RO_$_AAFPrivacySensitiveDictionaryLog
+ __OBJC_METACLASS_RO_$_AAFResponseBodyRedactor
+ __OBJC_PROTOCOL_$_AAFPrivacySensitiveLog
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$keysToRedact
+ _objc_msgSend$redactedCopyForObject:forKeys:
+ _objc_msgSend$redactedCopyForResponse:forKeys:
+ _objc_msgSend$response
CStrings:
+ "%@"
+ "<PRIVACY SENSITIVE>"
+ "@\"NSSet\""
+ "AAFPrivacySensitiveDictionaryLog"
+ "AAFPrivacySensitiveLog"
+ "AAFResponseBodyRedactor"
+ "T@\"NSDictionary\",R,N,V_response"
+ "T@\"NSSet\",R,N,V_keysToRedact"
+ "_keysToRedact"
+ "_response"
+ "arrayWithCapacity:"
+ "initWithDictionary:forKeys:"
+ "keysToRedact"
+ "redactedCopyForObject:forKeys:"
+ "redactedCopyForResponse:forKeys:"
+ "redactedDescription"
+ "response"

```

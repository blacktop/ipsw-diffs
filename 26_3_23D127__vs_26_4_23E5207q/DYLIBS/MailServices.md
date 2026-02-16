## MailServices

> `/System/Library/PrivateFrameworks/MailServices.framework/MailServices`

```diff

-3864.400.21.0.0
-  __TEXT.__text: 0xdc54
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0xe5c
-  __TEXT.__cstring: 0x18e8
+3864.500.147.2.3
+  __TEXT.__text: 0xe6e4
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__objc_methlist: 0xf3c
+  __TEXT.__cstring: 0x19b3
   __TEXT.__const: 0x8a
-  __TEXT.__gcc_except_tab: 0x1c10
+  __TEXT.__gcc_except_tab: 0x1cbc
   __TEXT.__dlopen_cstrs: 0x66
   __TEXT.__oslogstring: 0x680
-  __TEXT.__unwind_info: 0x9b8
-  __TEXT.__objc_classname: 0x277
-  __TEXT.__objc_methname: 0x2227
-  __TEXT.__objc_methtype: 0x723
+  __TEXT.__unwind_info: 0xa20
+  __TEXT.__objc_classname: 0x285
+  __TEXT.__objc_methname: 0x23c2
+  __TEXT.__objc_methtype: 0x741
   __TEXT.__objc_stubs: 0x1620
-  __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0xb58
-  __DATA_CONST.__objc_classlist: 0xa8
+  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__const: 0xb90
+  __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8a0
+  __DATA_CONST.__objc_selrefs: 0x8f8
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0xa0
+  __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x390
+  __AUTH_CONST.__auth_got: 0x370
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x1e00
-  __AUTH_CONST.__objc_const: 0x19b0
+  __AUTH_CONST.__cfstring: 0x1ee0
+  __AUTH_CONST.__objc_const: 0x1ba0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0xd8
-  __DATA.__objc_ivar: 0xe0
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0xf8
   __DATA.__data: 0x498
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x690

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EDE60E58-F7E3-3FC6-84FB-2D525829E1C0
-  Functions: 304
-  Symbols:   1643
-  CStrings:  1023
+  UUID: 438D2F1D-5864-38E1-8196-B81EFE9D3098
+  Functions: 321
+  Symbols:   1699
+  CStrings:  1062
 
Symbols:
+ +[MSAttachment supportsSecureCoding]
+ -[MSAttachment .cxx_destruct]
+ -[MSAttachment contentID]
+ -[MSAttachment data]
+ -[MSAttachment encodeWithCoder:]
+ -[MSAttachment filename]
+ -[MSAttachment initWithCoder:]
+ -[MSAttachment initWithData:filename:mimeType:contentID:]
+ -[MSAttachment mimeType]
+ -[MSAttachment setContentID:]
+ -[MSAttachment setData:]
+ -[MSAttachment setFilename:]
+ -[MSAttachment setMimeType:]
+ -[MSEmailModel attachments]
+ -[MSEmailModel existingDraftReference]
+ -[MSEmailModel setAttachments:]
+ -[MSEmailModel setExistingDraftReference:]
+ _MSAttachmentCodingKeyContentID
+ _MSAttachmentCodingKeyData
+ _MSAttachmentCodingKeyFilename
+ _MSAttachmentCodingKeyMimeType
+ _MSAttachmentCodingKeyVersion
+ _MSCodingKeyAttachments
+ _MSCodingKeyExistingDraftReference
+ _OBJC_CLASS_$_MSAttachment
+ _OBJC_IVAR_$_MSAttachment._contentID
+ _OBJC_IVAR_$_MSAttachment._data
+ _OBJC_IVAR_$_MSAttachment._filename
+ _OBJC_IVAR_$_MSAttachment._mimeType
+ _OBJC_IVAR_$_MSEmailModel._attachments
+ _OBJC_IVAR_$_MSEmailModel._existingDraftReference
+ _OBJC_METACLASS_$_MSAttachment
+ __OBJC_$_CLASS_METHODS_MSAttachment
+ __OBJC_$_CLASS_PROP_LIST_MSAttachment
+ __OBJC_$_INSTANCE_METHODS_MSAttachment
+ __OBJC_$_INSTANCE_VARIABLES_MSAttachment
+ __OBJC_$_PROP_LIST_MSAttachment
+ __OBJC_CLASS_PROTOCOLS_$_MSAttachment
+ __OBJC_CLASS_RO_$_MSAttachment
+ __OBJC_METACLASS_RO_$_MSAttachment
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
CStrings:
+ "@\"NSData\""
+ "@48@0:8@16@24@32@40"
+ "MSAttachment"
+ "MSAttachmentCodingKeyContentID"
+ "MSAttachmentCodingKeyData"
+ "MSAttachmentCodingKeyFilename"
+ "MSAttachmentCodingKeyMimeType"
+ "MSAttachmentCodingKeyVersion"
+ "MSCodingKeyAttachments"
+ "MSCodingKeyExistingDraftReference"
+ "T@\"NSArray\",C,N,V_attachments"
+ "T@\"NSData\",C,N,V_data"
+ "T@\"NSString\",C,N,V_contentID"
+ "T@\"NSString\",C,N,V_filename"
+ "T@\"NSString\",C,N,V_mimeType"
+ "T@\"NSURL\",&,N,V_existingDraftReference"
+ "_contentID"
+ "_data"
+ "_existingDraftReference"
+ "_filename"
+ "_mimeType"
+ "contentID"
+ "existingDraftReference"
+ "initWithData:filename:mimeType:contentID:"
+ "mimeType"
+ "setContentID:"
+ "setData:"
+ "setExistingDraftReference:"
+ "setFilename:"
+ "setMimeType:"

```

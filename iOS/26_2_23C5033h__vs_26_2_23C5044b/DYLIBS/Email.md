## Email

> `/System/Library/PrivateFrameworks/Email.framework/Email`

```diff

-3864.300.22.2.1
-  __TEXT.__text: 0xce640
+3864.300.41.2.1
+  __TEXT.__text: 0xce454
   __TEXT.__auth_stubs: 0x14f0
-  __TEXT.__objc_methlist: 0xc9b4
-  __TEXT.__gcc_except_tab: 0x1b1c8
+  __TEXT.__objc_methlist: 0xc95c
+  __TEXT.__gcc_except_tab: 0x1b18c
   __TEXT.__const: 0x1238
-  __TEXT.__cstring: 0xb62c
+  __TEXT.__cstring: 0xb64c
   __TEXT.__oslogstring: 0x6123
   __TEXT.__dlopen_cstrs: 0x10a
   __TEXT.__ustring: 0x154

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__unwind_info: 0x7a78
   __TEXT.__eh_frame: 0x1f8
-  __TEXT.__objc_classname: 0x1a44
-  __TEXT.__objc_methname: 0x1b2cf
-  __TEXT.__objc_methtype: 0x4714
-  __TEXT.__objc_stubs: 0x11d80
-  __DATA_CONST.__got: 0xca0
-  __DATA_CONST.__const: 0x4270
+  __TEXT.__objc_classname: 0x1a4a
+  __TEXT.__objc_methname: 0x1b35a
+  __TEXT.__objc_methtype: 0x470e
+  __TEXT.__objc_stubs: 0x11da0
+  __DATA_CONST.__got: 0xca8
+  __DATA_CONST.__const: 0x4278
   __DATA_CONST.__objc_classlist: 0x570
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x330
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5ea8
+  __DATA_CONST.__objc_selrefs: 0x5eb0
   __DATA_CONST.__objc_protorefs: 0x118
-  __DATA_CONST.__objc_superrefs: 0x478
+  __DATA_CONST.__objc_superrefs: 0x470
   __DATA_CONST.__objc_arraydata: 0x1e8
   __AUTH_CONST.__auth_got: 0xa88
   __AUTH_CONST.__const: 0x1848
-  __AUTH_CONST.__cfstring: 0x9be0
-  __AUTH_CONST.__objc_const: 0x16310
+  __AUTH_CONST.__cfstring: 0x9c00
+  __AUTH_CONST.__objc_const: 0x162f8
   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x618
+  __AUTH.__objc_data: 0x668
   __AUTH.__data: 0x158
   __DATA.__objc_ivar: 0xbdc
   __DATA.__data: 0x28a8
   __DATA.__bss: 0x1bb0
-  __DATA_DIRTY.__objc_data: 0x3200
+  __DATA_DIRTY.__objc_data: 0x31b0
   __DATA_DIRTY.__data: 0x1c0
   __DATA_DIRTY.__bss: 0x850
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7CD0FB52-54D2-3D55-8725-0F72C9798FC2
-  Functions: 4765
-  Symbols:   17728
-  CStrings:  8417
+  UUID: D2896D8C-7316-3199-96C7-43F86BAB976D
+  Functions: 4760
+  Symbols:   17720
+  CStrings:  8418
 
Symbols:
+ +[EMMessageBodyParsingUtils bodyElementChildThreshold]
+ +[EMMessageBodyParsingUtils nodeDepthThreshold]
+ +[EMMessageBodyParsingUtils priceFormattingThresholds]
+ +[EMMessageBodyParsingUtils snippetFromHTMLBody:options:maxLength:preservingQuotedForwardedContent:]
+ -[EMMailbox _commonInitName:accountIdentifier:type:canContainMessages:parentID:builder:]
+ -[EMQuery _publicDescription]
+ -[EMQuery description]
+ -[EMQuery ef_publicDescription]
+ _EMUserDefaultShowSearchFeedbackPrompt
+ _OBJC_CLASS_$_ECMessageBodyParsingUtils
+ _OBJC_CLASS_$_ECPriceFormattingThresholds
+ _OBJC_CLASS_$_EMMessageBodyParsingUtils
+ _OBJC_IVAR_$_EMQuery._publicDescription
+ _OBJC_METACLASS_$_EMMessageBodyParsingUtils
+ __OBJC_$_CLASS_METHODS_EMMessageBodyParsingUtils
+ __OBJC_$_CLASS_PROP_LIST_EMMessageBodyParsingUtils
+ __OBJC_CLASS_RO_$_EMMessageBodyParsingUtils
+ __OBJC_METACLASS_RO_$_EMMessageBodyParsingUtils
+ ___block_literal_global.418
+ _objc_msgSend$_commonInitName:accountIdentifier:type:canContainMessages:parentID:builder:
+ _objc_msgSend$bodyElementChildThreshold
+ _objc_msgSend$initWithNodeDepthThreshold:bodyChildCountThreshold:
+ _objc_msgSend$nodeDepthThreshold
+ _objc_msgSend$priceFormattingThresholds
+ _objc_msgSend$snippetFromHTMLBody:options:maxLength:preservingQuotedForwardedContent:priceFormattingThresholds:
- +[EMMailboxCollection supportsSecureCoding]
- -[EMMailbox _commonInitName:accountIdentifier:type:canContainMessages:children:parentID:builder:]
- -[EMMailbox children]
- -[EMMailbox setChildren:]
- -[EMMailboxCollection encodeWithCoder:]
- -[EMMailboxCollection initWithAccount:topLevelOnly:]
- -[EMMailboxCollection initWithAccount:topLevelOnly:repository:]
- -[EMMailboxCollection initWithCoder:]
- -[EMMailboxCollection initWithMailbox:]
- -[EMMailboxCollection initWithMailbox:repository:]
- -[EMMailboxCollection initWithObjectID:query:]
- -[EMMailboxCollection(EMRepositoryObjectSubclass) repository]
- -[EMMailboxCollection(EMRepositoryObjectSubclass) setRepository:]
- _OBJC_CLASS_$_EMMailboxCollection
- _OBJC_IVAR_$_EMMailbox._children
- _OBJC_METACLASS_$_EMMailboxCollection
- __OBJC_$_CLASS_METHODS_EMMailboxCollection
- __OBJC_$_CLASS_PROP_LIST_EMMailboxCollection
- __OBJC_$_INSTANCE_METHODS_EMMailboxCollection(EMRepositoryObjectSubclass)
- __OBJC_CLASS_PROTOCOLS_$_EMMailboxCollection
- __OBJC_CLASS_RO_$_EMMailboxCollection
- __OBJC_METACLASS_RO_$_EMMailboxCollection
- ___block_literal_global.415
- _objc_msgSend$_commonInitName:accountIdentifier:type:canContainMessages:children:parentID:builder:
- _objc_msgSend$children
- _objc_msgSend$initWithAccount:topLevelOnly:repository:
- _objc_msgSend$initWithMailbox:repository:
- _objc_msgSend$predicateForMailboxChildren:
CStrings:
+ "@44@0:8@16Q24Q32B40"
+ "EMMessageBodyParsingUtils"
+ "ShowSearchFeedbackPrompt"
+ "T@\"ECPriceFormattingThresholds\",R"
+ "_commonInitName:accountIdentifier:type:canContainMessages:parentID:builder:"
+ "_publicDescription"
+ "bodyElementChildThreshold"
+ "initWithNodeDepthThreshold:bodyChildCountThreshold:"
+ "nodeDepthThreshold"
+ "price-formatting-check-body-child-count-threshold"
+ "price-formatting-check-node-depth-threshold"
+ "priceFormattingThresholds"
+ "snippetFromHTMLBody:options:maxLength:preservingQuotedForwardedContent:"
+ "snippetFromHTMLBody:options:maxLength:preservingQuotedForwardedContent:priceFormattingThresholds:"
+ "v60@0:8@16@24q32B40@44@?52"
- "-[EMMailboxCollection initWithObjectID:query:]"
- "@\"EMMailboxCollection\""
- "EFPropertyKey_children"
- "EMMailboxCollection"
- "EMMailboxCollection.m"
- "T@\"EMMailboxCollection\",&,N,V_children"
- "T@\"EMMailboxRepository\",R,N"
- "_children"
- "_commonInitName:accountIdentifier:type:canContainMessages:children:parentID:builder:"
- "children"
- "initWithAccount:topLevelOnly:"
- "initWithAccount:topLevelOnly:repository:"
- "initWithMailbox:repository:"
- "setChildren:"
- "v68@0:8@16@24q32B40@44@52@?60"

```

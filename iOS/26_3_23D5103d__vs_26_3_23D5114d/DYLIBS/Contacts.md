## Contacts

> `/System/Library/Frameworks/Contacts.framework/Contacts`

```diff

-3804.400.11.0.0
-  __TEXT.__text: 0x1bd30c
+3804.400.41.0.0
+  __TEXT.__text: 0x1bd89c
   __TEXT.__auth_stubs: 0x3350
-  __TEXT.__objc_methlist: 0x1b178
+  __TEXT.__objc_methlist: 0x1b1a8
   __TEXT.__const: 0x24c0
   __TEXT.__gcc_except_tab: 0x3bbc
-  __TEXT.__cstring: 0xcb32
+  __TEXT.__cstring: 0xcb52
   __TEXT.__dlopen_cstrs: 0x8ba
   __TEXT.__oslogstring: 0xc23a
   __TEXT.__ustring: 0x12

   __TEXT.__swift_as_ret: 0x5c
   __TEXT.__unwind_info: 0x7fe0
   __TEXT.__eh_frame: 0x2610
-  __TEXT.__objc_classname: 0x44c0
-  __TEXT.__objc_methname: 0x2ba7d
-  __TEXT.__objc_methtype: 0x5426
-  __TEXT.__objc_stubs: 0x1eda0
+  __TEXT.__objc_classname: 0x44bd
+  __TEXT.__objc_methname: 0x2bb30
+  __TEXT.__objc_methtype: 0x5436
+  __TEXT.__objc_stubs: 0x1ee20
   __DATA_CONST.__got: 0x1ba0
   __DATA_CONST.__const: 0x61e8
   __DATA_CONST.__objc_classlist: 0x1118
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x300
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9860
+  __DATA_CONST.__objc_selrefs: 0x9870
   __DATA_CONST.__objc_protorefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x9c0
   __DATA_CONST.__objc_arraydata: 0x268
   __AUTH_CONST.__auth_got: 0x19b8
   __AUTH_CONST.__const: 0x6b78
-  __AUTH_CONST.__cfstring: 0xda60
-  __AUTH_CONST.__objc_const: 0x2c1f0
+  __AUTH_CONST.__cfstring: 0xda80
+  __AUTH_CONST.__objc_const: 0x2c260
   __AUTH_CONST.__objc_intobj: 0x5d0
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x5868
   __AUTH.__data: 0x660
-  __DATA.__objc_ivar: 0x1284
+  __DATA.__objc_ivar: 0x128c
   __DATA.__data: 0x2cd0
   __DATA.__bss: 0x24d0
   __DATA.__common: 0x80

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8BB23EE3-DACD-3B63-A91C-D4F6441F5AF9
-  Functions: 12583
-  Symbols:   36872
-  CStrings:  12914
+  UUID: F6CCEC79-8988-333E-8C80-1B805F06C613
+  Functions: 12586
+  Symbols:   36884
+  CStrings:  12924
 
Symbols:
+ +[CNContactBufferDecoderFactory decoderForFetchRequest:]
+ -[CNContact uuid]
+ -[CNContactBufferDecoder initWithKeyDescriptorToMakeAvailable:mutableResults:]
+ -[CNiOSABContactBuffersDecoder _populatePosterDataSourceDataIfNeededForContacts:]
+ -[CNiOSABContactBuffersDecoder initWithDecoder:unifyResults:unificationOptions:mutableResults:decodeBatchLimit:requestedKeys:posterDataStore:]
+ -[CNiOSABContactBuffersDecoder posterDataStore]
+ -[CNiOSABContactBuffersDecoder requestedKeys]
+ GCC_except_table151
+ _OBJC_IVAR_$_CNContact._uuid
+ _OBJC_IVAR_$_CNiOSABContactBuffersDecoder._posterDataStore
+ _OBJC_IVAR_$_CNiOSABContactBuffersDecoder._requestedKeys
+ ___17-[CNContact uuid]_block_invoke
+ ___57-[CNiOSABContactBuffersDecoder unifyContacts:moreComing:]_block_invoke.22
+ ___block_literal_global.254
+ ___block_literal_global.308
+ ___block_literal_global.311
+ ___block_literal_global.318
+ ___block_literal_global.329
+ ___block_literal_global.804
+ ___block_literal_global.867
+ ___block_literal_global.876
+ _objc_msgSend$_populatePosterDataSourceDataIfNeededForContacts:
+ _objc_msgSend$decoderForFetchRequest:
+ _objc_msgSend$initWithDecoder:unifyResults:unificationOptions:mutableResults:decodeBatchLimit:requestedKeys:posterDataStore:
+ _objc_msgSend$initWithKeyDescriptorToMakeAvailable:mutableResults:
+ _objc_msgSend$requestedKeys
+ _objc_msgSend$setMutableResults:
+ _objc_msgSend$uuidFromContactIdentifier:
- +[CNContactBufferDecoderFactory decoderForFetchRequest:posterDataStore:]
- -[CNContactBufferDecoder addContactImageDataToContact:]
- -[CNContactBufferDecoder addPosterDataToContact:]
- -[CNContactBufferDecoder initWithKeyDescriptorToMakeAvailable:posterDataStore:mutableResults:]
- -[CNiOSABContactBuffersDecoder initWithDecoder:unifyResults:unificationOptions:mutableResults:decodeBatchLimit:]
- GCC_except_table149
- _OBJC_IVAR_$_CNContactBufferDecoder._posterDataStore
- ___57-[CNiOSABContactBuffersDecoder unifyContacts:moreComing:]_block_invoke.13
- ___block_literal_global.252
- ___block_literal_global.296
- ___block_literal_global.306
- ___block_literal_global.309
- ___block_literal_global.797
- ___block_literal_global.860
- ___block_literal_global.869
- _objc_msgSend$decoderForFetchRequest:posterDataStore:
- _objc_msgSend$initWithDecoder:unifyResults:unificationOptions:mutableResults:decodeBatchLimit:
- _objc_msgSend$initWithKeyDescriptorToMakeAvailable:posterDataStore:mutableResults:
CStrings:
+ "@\"NSUUID\""
+ "@64@0:8@16B24@28B36q40@48@56"
+ "Expected class of %@ but was %@"
+ "T@\"<CNContactPosterDataStore>\",R,V_posterDataStore"
+ "T@\"NSArray\",R,V_requestedKeys"
+ "T@\"NSUUID\",R,C"
+ "_populatePosterDataSourceDataIfNeededForContacts:"
+ "_requestedKeys"
+ "_uuid"
+ "decoderForFetchRequest:"
+ "initWithDecoder:unifyResults:unificationOptions:mutableResults:decodeBatchLimit:requestedKeys:posterDataStore:"
+ "initWithKeyDescriptorToMakeAvailable:mutableResults:"
+ "requestedKeys"
- "@48@0:8@16B24@28B36q40"
- "decoderForFetchRequest:posterDataStore:"
- "initWithDecoder:unifyResults:unificationOptions:mutableResults:decodeBatchLimit:"
- "initWithKeyDescriptorToMakeAvailable:posterDataStore:mutableResults:"

```

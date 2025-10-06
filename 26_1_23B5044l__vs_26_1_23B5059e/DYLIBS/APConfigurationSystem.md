## APConfigurationSystem

> `/System/Library/PrivateFrameworks/APConfigurationSystem.framework/APConfigurationSystem`

```diff

-556.1.3.0.0
-  __TEXT.__text: 0xbb1c
-  __TEXT.__auth_stubs: 0x910
-  __TEXT.__objc_methlist: 0xc3c
-  __TEXT.__const: 0xc78
-  __TEXT.__cstring: 0xd87
-  __TEXT.__oslogstring: 0xaad
+556.1.10.0.0
+  __TEXT.__text: 0xdf2c
+  __TEXT.__auth_stubs: 0xb30
+  __TEXT.__objc_methlist: 0xca4
+  __TEXT.__const: 0xd58
+  __TEXT.__cstring: 0x10ae
+  __TEXT.__oslogstring: 0xbda
   __TEXT.__gcc_except_tab: 0x4c
-  __TEXT.__swift5_typeref: 0x2f2
-  __TEXT.__swift5_fieldmd: 0x350
-  __TEXT.__constg_swiftt: 0x400
+  __TEXT.__swift5_typeref: 0x342
+  __TEXT.__constg_swiftt: 0x478
+  __TEXT.__swift5_reflstr: 0x29f
+  __TEXT.__swift5_fieldmd: 0x384
+  __TEXT.__swift5_types: 0x50
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__swift5_reflstr: 0x24f
-  __TEXT.__swift5_proto: 0x9c
-  __TEXT.__swift5_types: 0x4c
+  __TEXT.__swift5_proto: 0xa4
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x408
+  __TEXT.__unwind_info: 0x470
   __TEXT.__eh_frame: 0x108
-  __TEXT.__objc_classname: 0x4b3
-  __TEXT.__objc_methname: 0x1c22
-  __TEXT.__objc_methtype: 0x387
-  __TEXT.__objc_stubs: 0x1540
-  __DATA_CONST.__got: 0x1d0
+  __TEXT.__objc_classname: 0x4b1
+  __TEXT.__objc_methname: 0x1d45
+  __TEXT.__objc_methtype: 0x3ad
+  __TEXT.__objc_stubs: 0x1620
+  __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__const: 0x1d8
-  __DATA_CONST.__objc_classlist: 0x198
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x708
+  __DATA_CONST.__objc_selrefs: 0x750
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x498
-  __AUTH_CONST.__const: 0x650
+  __AUTH_CONST.__auth_got: 0x5a8
+  __AUTH_CONST.__const: 0x678
   __AUTH_CONST.__cfstring: 0xb40
-  __AUTH_CONST.__objc_const: 0x3368
+  __AUTH_CONST.__objc_const: 0x3448
   __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH.__objc_data: 0x1e0
-  __AUTH.__data: 0xd8
-  __DATA.__objc_ivar: 0x58
-  __DATA.__data: 0x350
-  __DATA.__bss: 0xc80
-  __DATA_DIRTY.__objc_data: 0xc30
+  __AUTH.__objc_data: 0x2c0
+  __AUTH.__data: 0x100
+  __DATA.__objc_ivar: 0x5c
+  __DATA.__data: 0x3b0
+  __DATA.__bss: 0xd80
+  __DATA_DIRTY.__objc_data: 0xc58
   __DATA_DIRTY.__data: 0x3a8
   __DATA_DIRTY.__bss: 0x510
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B2B58DEA-0705-364D-8C5A-B93482E5E406
-  Functions: 400
-  Symbols:   265
-  CStrings:  733
+  UUID: CE6FD469-87B6-3160-B258-7205B330ACBD
+  Functions: 451
+  Symbols:   286
+  CStrings:  774
 
Symbols:
+ _NSCocoaErrorDomain
+ _OBJC_CLASS_$_APConfigurationStorefrontValidator
+ _OBJC_METACLASS_$_APConfigurationStorefrontValidator
+ __swiftImmortalRefCount
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_reportUnimplementedInitializer
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_retain_x27
+ _swift_arrayDestroy
+ _swift_beginAccess
+ _swift_bridgeObjectRetain
+ _swift_endAccess
+ _swift_errorRetain
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_isaMask
+ _swift_unknownObjectRetain
+ _swift_updateClassMetadata2
- _objc_retain_x26
CStrings:
+ "$__lazy_storage_$_url"
+ "@\"APConfigurationStorefrontValidator\""
+ "APConfigurationStorefrontValidator"
+ "APConfigurationSystem.ConfigurationStorefrontValidator"
+ "Congfiguration Error: %@ Node: %s. Error description: %s."
+ "Error Decoding configuration"
+ "Error creating XPC Listener."
+ "Error decoding XPC Message."
+ "Error deserializing data"
+ "Error getting URL for Configuration Host."
+ "Error no XPC Session available."
+ "Error no configuration found for path."
+ "Error on XPC Request."
+ "Error parsing Configuration File."
+ "Error reading storefront from filesystem, description: "
+ "Error saving storefront to filesystem, description: "
+ "Error serializing data"
+ "Error: Configuration processing failed."
+ "Properties not found in node."
+ "Session not available."
+ "Storefront change detected, reseting configuration."
+ "T@\"APConfigurationStorefrontValidator\",R,N,V_storefrontValidator"
+ "[ConfigurationStorefrontValidator] Old storefront empty."
+ "[ConfigurationStorefrontValidator] Old storefront: %{public}s"
+ "[ConfigurationStorefrontValidator] Storefront: %{public}s saved to filesystem."
+ "_mockConfigurationServerResponseIfNeeded"
+ "_resetConfigurationForStorefrontChangeIfNeeded"
+ "_storefrontValidator"
+ "code"
+ "configurationNeedsReset"
+ "configurationPath"
+ "dealloc"
+ "domain"
+ "init()"
+ "initWithStorefront:configurationPath:"
+ "saveStorefront"
+ "storefrontValidator"
- "Return configuration from framework defaults."

```

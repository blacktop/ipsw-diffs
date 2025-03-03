## DialogEngine

> `/System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine`

```diff

-3404.10.1.1.1
-  __TEXT.__text: 0x4f8ad8
-  __TEXT.__auth_stubs: 0x2090
-  __TEXT.__init_offsets: 0x24
+3404.15.1.0.0
+  __TEXT.__text: 0x4f9358
+  __TEXT.__auth_stubs: 0x20a0
+  __TEXT.__init_offsets: 0x28
   __TEXT.__objc_methlist: 0x335c
-  __TEXT.__const: 0x1b983
-  __TEXT.__cstring: 0x6619c
-  __TEXT.__gcc_except_tab: 0x3c678
+  __TEXT.__const: 0x1ba3b
+  __TEXT.__cstring: 0x66252
+  __TEXT.__gcc_except_tab: 0x3c78c
   __TEXT.__oslogstring: 0x2bf
   __TEXT.__ustring: 0xaa
-  __TEXT.__unwind_info: 0x13e30
+  __TEXT.__unwind_info: 0x13ea0
   __TEXT.__objc_classname: 0x4de
-  __TEXT.__objc_methname: 0x6a61
+  __TEXT.__objc_methname: 0x6a9c
   __TEXT.__objc_methtype: 0x5f55
-  __TEXT.__objc_stubs: 0x41c0
-  __DATA_CONST.__got: 0x598
+  __TEXT.__objc_stubs: 0x4240
+  __DATA_CONST.__got: 0x5a8
   __DATA_CONST.__const: 0x3108
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18a8
+  __DATA_CONST.__objc_selrefs: 0x18c8
   __DATA_CONST.__objc_superrefs: 0x170
   __DATA_CONST.__objc_arraydata: 0x188
-  __AUTH_CONST.__auth_got: 0x1060
+  __AUTH_CONST.__auth_got: 0x1068
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x128a8
+  __AUTH_CONST.__const: 0x12948
   __AUTH_CONST.__cfstring: 0x1ae0
   __AUTH_CONST.__objc_const: 0x62a8
   __AUTH_CONST.__objc_arrayobj: 0x1f8

   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
   __DATA.__objc_ivar: 0x3b4
-  __DATA.__data: 0x530
+  __DATA.__data: 0x570
   __DATA.__common: 0x1288
-  __DATA.__bss: 0x3168
+  __DATA.__bss: 0x3538
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0x17f8
   __DATA_DIRTY.__common: 0x29b0
-  __DATA_DIRTY.__bss: 0x1a8
+  __DATA_DIRTY.__bss: 0x238
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 15442
-  Symbols:   18111
-  CStrings:  28158
+  Functions: 15461
+  Symbols:   18136
+  CStrings:  28166
 
Symbols:
+ _CNContactPronunciationFamilyNameKey
+ _CNContactPronunciationGivenNameKey
+ __ZN4siri12dialogengine10LineNumberERKN4YAML4NodeE
+ __ZN4siri12dialogengine10LineNumberERKN4YAML9ExceptionE
+ __ZN4siri12dialogengine12ColumnNumberERKN4YAML9ExceptionE
+ __ZN4siri12dialogengine16ExceptionDetailsERKN4YAML9ExceptionERKNSt3__112basic_stringIcNS5_11char_traitsIcEENS5_9allocatorIcEEEE
+ __ZN4siri12dialogengine6MeCard17GetMeCardProviderEv
+ __ZN4siri12dialogengine6MeCard17SetMeCardProviderENSt3__110shared_ptrINS0_14MeCardProviderEEE
+ __ZNK4siri12dialogengine21DefaultMeCardProvider9GetMeCardEv
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEl
+ __ZTIN4siri12dialogengine21DefaultMeCardProviderE
+ __ZTSN4siri12dialogengine21DefaultMeCardProviderE
+ __ZTVN4siri12dialogengine21DefaultMeCardProviderE
CStrings:
+ "\n- code: "
+ "\n- domain: "
+ "\n- localizedDescription: "
+ "\n- localizedFailureReason: "
+ " / "
+ "3404.15.1"
+ "CAT Request (Dialog Engine 3404.15.1)"
+ "Column: "
+ "Could not parse YAML file: "
+ "Failed to get MeCard from CNContactStore"
+ "Set the name of the variable returned from the callback function to the full keyPath string: '%s'"
+ "YAML::Exception"
+ "domain"
+ "parameter/redacted"
+ "pronunciationFamilyName"
+ "pronunciationGivenName"
+ "yaml-cpp exception in YAML file: "
- "\nError: "
- "    Column: "
- "    Error: "
- "    Line: "
- "    Path: "
- "3404.10.1"
- "CAT Request (Dialog Engine 3404.10.1)"
- "Could not parse YAML file\n"
- "Could not parse YAML file "
- "yaml-cpp exception in YAML file:"

```

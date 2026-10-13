## companiond

> `usr/libexec/companiond`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-524.10.109.0.1
-  __TEXT.__text: 0x85c24
-  __TEXT.__auth_stubs: 0x2d40
-  __TEXT.__objc_stubs: 0x4460
-  __TEXT.__objc_methlist: 0x2b60
-  __TEXT.__objc_methname: 0x61a5
+524.11.6.0.0
+  __TEXT.__text: 0x8774c
+  __TEXT.__auth_stubs: 0x2d50
+  __TEXT.__objc_stubs: 0x45a0
+  __TEXT.__objc_methlist: 0x2d30
+  __TEXT.__objc_methname: 0x6475
   __TEXT.__swift5_typeref: 0xcbb
   __TEXT.__swift5_fieldmd: 0x820
-  __TEXT.__objc_classname: 0xb48
-  __TEXT.__objc_methtype: 0x159b
+  __TEXT.__objc_classname: 0xb9b
+  __TEXT.__objc_methtype: 0x15fd
   __TEXT.__const: 0x20d6
   __TEXT.__constg_swiftt: 0x7ec
   __TEXT.__swift5_reflstr: 0x832
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__cstring: 0x2621
+  __TEXT.__cstring: 0x2789
   __TEXT.__swift5_capture: 0x754
   __TEXT.__swift5_assocty: 0x150
   __TEXT.__swift5_proto: 0x118

   __TEXT.__swift_as_entry: 0x1b0
   __TEXT.__swift_as_ret: 0x1d0
   __TEXT.__swift_as_cont: 0x3a8
-  __TEXT.__oslogstring: 0x4142
+  __TEXT.__oslogstring: 0x426e
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__gcc_except_tab: 0x1ad0
+  __TEXT.__gcc_except_tab: 0x1c50
   __TEXT.__ustring: 0x40
-  __TEXT.__unwind_info: 0x2b40
+  __TEXT.__unwind_info: 0x2bb8
   __TEXT.__eh_frame: 0x4eb8
-  __DATA_CONST.__const: 0x2538
-  __DATA_CONST.__cfstring: 0x1ba0
-  __DATA_CONST.__objc_classlist: 0x240
+  __DATA_CONST.__const: 0x2580
+  __DATA_CONST.__cfstring: 0x1ce0
+  __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x198
+  __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x16b0
-  __DATA_CONST.__got: 0xcf8
+  __DATA_CONST.__auth_got: 0x16b8
+  __DATA_CONST.__got: 0xd00
   __DATA_CONST.__auth_ptr: 0x560
-  __DATA.__objc_const: 0x7568
-  __DATA.__objc_selrefs: 0x1560
-  __DATA.__objc_ivar: 0x414
-  __DATA.__objc_data: 0x18e0
+  __DATA.__objc_const: 0x7988
+  __DATA.__objc_selrefs: 0x15e0
+  __DATA.__objc_ivar: 0x440
+  __DATA.__objc_data: 0x1980
   __DATA.__data: 0x1df0
   __DATA.__common: 0xe8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   - @rpath/AppleConnectClient.framework/AppleConnectClient
-  Functions: 2295
-  Symbols:   1269
-  CStrings:  1956
+  Functions: 2341
+  Symbols:   1271
+  CStrings:  1997
 
Symbols:
+ _CPSAllowedClassesForPhotosConfiguration
+ _OBJC_CLASS_$_CPSPhotosConfigurationRequest
CStrings:
+ "@\"<CPSPhotosConfiguration>\""
+ "@\"CPSPhotosConfigurationRequest\""
+ "CDPhotosConfigurationDidFinishAuthRequest"
+ "CDPhotosConfigurationGetAuthInfoResponse"
+ "CompanionViewService.PhotosConfigurationViewController"
+ "Missing configuration in get auth info response: %@"
+ "PHOTOS_CONFIGURATION_BODY"
+ "PHOTOS_CONFIGURATION_TITLE"
+ "Photos configuration completion {configuration = %@, error = %@}"
+ "Starting Photos Configuration session."
+ "T@\"<CPSPhotosConfiguration>\",C,N,V_configuration"
+ "T@\"CPSPhotosConfigurationRequest\",&,N,V_photosConfigurationRequest"
+ "T@?,C,N,V_photosConfigurationCompletionHandler"
+ "[decodedResponse configuration]"
+ "_photosConfigurationCompletionHandler"
+ "_photosConfigurationRequest"
+ "_photosConfigurationUserNotificationSessionWithGetAuthInfoResponse:"
+ "_presentPhotosConfigurationViewService:proxCardClient:"
+ "_typeIdentifierForDevice:"
+ "appletv"
+ "com.apple.companion-authentication.photos-configuration"
+ "com.apple.homeaccessory-1"
+ "com.apple.homeaccessory-2"
+ "hasPhotosConfigurationEntitlement"
+ "initWithConfiguration:"
+ "localizedDescription"
+ "person.badge.waveform.fill"
+ "photoSetupContentWithTypeIdentifier:"
+ "photos configuration session/handle get auth info response"
+ "photos configuration session/present view service"
+ "photos configuration session/start"
+ "photosConfigurationCompletionHandler"
+ "photosConfigurationContent"
+ "photosConfigurationFailedWithError:"
+ "photosConfigurationFinishedWithConfiguration:"
+ "photosConfigurationObject"
+ "photosConfigurationRequest"
+ "setConfiguration:"
+ "setPhotosConfigurationCompletionHandler:"
+ "setPhotosConfigurationRequest:"
+ "typeWithIdentifier:"
+ "v24@0:8@\"<CPSPhotosConfiguration>\"16"
+ "v24@?0@\"<CPSPhotosConfiguration>\"8@\"NSError\"16"
- "photoSetupContent"
- "siri-icon"
```

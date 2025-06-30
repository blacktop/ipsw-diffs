## locationd

> `/usr/libexec/locationd`

```diff

-2890.16.16.0.0
-  __TEXT.__text: 0x1b3781c
+2890.16.23.0.0
+  __TEXT.__text: 0x1b3955c
   __TEXT.__auth_stubs: 0x68e0
-  __TEXT.__objc_stubs: 0x3e260
+  __TEXT.__objc_stubs: 0x3e2e0
   __TEXT.__init_offsets: 0x6b8
-  __TEXT.__objc_methlist: 0x25a74
+  __TEXT.__objc_methlist: 0x25aa4
   __TEXT.__const: 0x155281
-  __TEXT.__gcc_except_tab: 0xbab84
-  __TEXT.__objc_methname: 0x57a9a
+  __TEXT.__gcc_except_tab: 0xbad4c
+  __TEXT.__objc_methname: 0x57b78
   __TEXT.__objc_classname: 0x759c
-  __TEXT.__objc_methtype: 0x3f1e4
-  __TEXT.__cstring: 0x1c8489
-  __TEXT.__oslogstring: 0x24ddbe
+  __TEXT.__objc_methtype: 0x3f20a
+  __TEXT.__cstring: 0x1c85da
+  __TEXT.__oslogstring: 0x24e2c8
   __TEXT.__constg_swiftt: 0xec
   __TEXT.__swift5_typeref: 0xad
   __TEXT.__swift5_fieldmd: 0x30
   __TEXT.__swift5_types: 0x10
   __TEXT.__dlopen_cstrs: 0xa0
   __TEXT.__ustring: 0x2ee
-  __TEXT.__unwind_info: 0x62ba4
+  __TEXT.__unwind_info: 0x62bf8
   __TEXT.__eh_frame: 0x1020
   __DATA_CONST.__linkguard: 0x15
   __DATA.__auth_got: 0x3488
   __DATA.__got: 0x1be0
   __DATA.__auth_ptr: 0x2f0
   __DATA.__const: 0xb3300
-  __DATA.__cfstring: 0x37a40
+  __DATA.__cfstring: 0x37aa0
   __DATA.__objc_classlist: 0x1320
   __DATA.__objc_catlist: 0xb8
   __DATA.__objc_protolist: 0xd40
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x53ee0
-  __DATA.__objc_selrefs: 0x12af8
+  __DATA.__objc_const: 0x53f60
+  __DATA.__objc_selrefs: 0x12b18
   __DATA.__objc_protorefs: 0x9f0
   __DATA.__objc_classrefs: 0x1db8
   __DATA.__objc_superrefs: 0x1170

   - /usr/lib/swift/libswiftSystem.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 5F5302D2-FACA-3799-B708-C5F436381DB3
-  Functions: 91049
+  UUID: BA54EE65-4551-3B88-A2C0-95433740D7FB
+  Functions: 91058
   Symbols:   3166
-  CStrings:  85800
+  CStrings:  85828
 
CStrings:
+ "#Spi, Must provide a bundle identifier or bundle path if setting temporay precise authorization"
+ "#Spi, Must provide a bundle identifier or bundle path if tearing down location auth prompt"
+ "-[CLInternalService setTemporaryPreciseAuthorizationGranted:forBundleID:orBundlePath:replyBlock:]"
+ "-[CLInternalService tearDownLocationAuthPromptForBundleID:orBundlePath:replyBlock:]"
+ "/AppleInternal/Library/BuildRoots/8bb5d799-4029-11ef-93f2-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/throw_on_empty_input.hpp"
+ "/AppleInternal/Library/BuildRoots/8bb5d799-4029-11ef-93f2-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
+ "/AppleInternal/Library/BuildRoots/8bb5d799-4029-11ef-93f2-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
+ "/AppleInternal/Library/BuildRoots/8bb5d799-4029-11ef-93f2-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/8bb5d799-4029-11ef-93f2-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
+ "/System/Library/PrivateFrameworks/AssistantServices.framework"
+ "19:48:22"
+ "19:54:22"
+ "@WifiLogic, registering for leeched Cell location notification"
+ "@WifiLogic, unregistering for leeched Cell location notification"
+ "CL: _CLDaemonSetTemporaryPreciseAuthorization (Fallback)"
+ "CL: _CLDaemonTearDownLocationAuthPrompt (Fallback)"
+ "Finished #AuthDatabaseMigration_8"
+ "Jul 14 2024"
+ "Jul 14 2024 19:57:03"
+ "Running #AuthDatabaseMigration_8"
+ "Siri needs to be reset"
+ "TearDown SPI Invocation"
+ "markTemporaryPreciseAuthorizationGranted:forClientKey:"
+ "setTemporaryPreciseAuthorizationGranted:forBundleID:orBundlePath:replyBlock:"
+ "tearDownLocationAuthPrompt:"
+ "tearDownLocationAuthPromptForBundleID:orBundlePath:replyBlock:"
+ "v28@0:8B16@\"NSString\"20"
+ "v28@0:8B16@20"
+ "void CLClientManager::migrateAuthDatabase_8()"
+ "{\"msg%{public}.0s\":\"#AuthDatabaseMigration_8 Siri authorization cleared\"}"
+ "{\"msg%{public}.0s\":\"#AuthDatabaseMigration_8 Siri has a user-set authorization value; not clearing.\"}"
+ "{\"msg%{public}.0s\":\"#AuthPrompt Teardown Inflight Prompt\", \"Client\":%{public, location:escape_only}s, \"PromptType\":%{public, location:CLClientManager_Type::AuthorizationRequestType}lld, \"Teardown Reason\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#AuthPrompt skip Teardown Inflight Prompt - actual and expected inflight client does not match\", \"ActualInflightClient\":%{public, location:escape_only}s, \"ExpectedInflightClient\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#ClearingAuthorization and corrective compensation\", \"Client\":%{public, location:escape_only}@, \"forceSyncToPairedDevice\":%{public}hhd, \"Reason\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#TemporaryAuth-Precise\", \"Client\":%{public, location:escape_only}@, \"granted\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"_CLDaemonSetTemporaryPreciseAuthorization\", \"event\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"_CLDaemonTearDownLocationAuthPrompt\", \"event\":%{public, location:escape_only}s}"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/throw_on_empty_input.hpp"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
- "07:38:56"
- "07:46:43"
- "@WifiLogic, registering for Cell location notification"
- "@WifiLogic, unregistering for Cell location notification"
- "May  2 2024"
- "May  2 2024 07:49:43"
- "{\"msg%{public}.0s\":\"#AuthPrompt Teardown Inflight Prompt\", \"ClientKey\":%{public, location:escape_only}s, \"PromptType\":%{public, location:CLClientManager_Type::AuthorizationRequestType}lld, \"Teardown Reason\":%{public, location:PromptTeardownReason}lld}"

```

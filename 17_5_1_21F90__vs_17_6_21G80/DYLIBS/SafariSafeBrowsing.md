## SafariSafeBrowsing

> `/System/Library/PrivateFrameworks/SafariSafeBrowsing.framework/SafariSafeBrowsing`

```diff

-7618.2.12.10.9
-  __TEXT.__text: 0x55f00
-  __TEXT.__auth_stubs: 0xf20
-  __TEXT.__objc_methlist: 0x794
-  __TEXT.__gcc_except_tab: 0x4e7c
-  __TEXT.__cstring: 0x2c45
-  __TEXT.__const: 0x218
-  __TEXT.__oslogstring: 0x1ab2
-  __TEXT.__unwind_info: 0x29e0
+618.3.11.10.5
+  __TEXT.__text: 0x56c3c
+  __TEXT.__auth_stubs: 0xf40
+  __TEXT.__objc_methlist: 0x7c4
+  __TEXT.__gcc_except_tab: 0x5068
+  __TEXT.__cstring: 0x2d4d
+  __TEXT.__const: 0x228
+  __TEXT.__oslogstring: 0x1c74
+  __TEXT.__unwind_info: 0x2a50
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x1eb
-  __TEXT.__objc_methname: 0x22b4
+  __TEXT.__objc_methname: 0x2376
   __TEXT.__objc_methtype: 0x162f
   __TEXT.__objc_stubs: 0x1720
   __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0x5e8
+  __DATA_CONST.__const: 0x608
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x15b0
-  __DATA_CONST.__objc_selrefs: 0x768
-  __DATA_CONST.__objc_classrefs: 0x130
+  __DATA_CONST.__objc_const: 0x15d0
+  __DATA_CONST.__objc_selrefs: 0x788
+  __DATA_CONST.__objc_classrefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__cfstring: 0xf20
+  __AUTH_CONST.__cfstring: 0x1020
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__const: 0xf78
+  __AUTH_CONST.__const: 0xfd8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x7a8
+  __AUTH_CONST.__auth_got: 0x7b8
   __DATA.__objc_ivar: 0x80
   __DATA.__data: 0x328
-  __DATA.__bss: 0x20
-  __DATA_DIRTY.__const: 0x13b8
+  __DATA.__bss: 0x40
+  __DATA_DIRTY.__const: 0x1398
   __DATA_DIRTY.__objc_const: 0x5d0
   __DATA_DIRTY.__objc_data: 0x410
   __DATA_DIRTY.__bss: 0x380

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A988F52D-61E6-32B1-BE80-404A07E25891
-  Functions: 2299
-  Symbols:   6026
-  CStrings:  1054
+  UUID: 81571455-432A-3AE1-B39D-03D3797760FA
+  Functions: 2317
+  Symbols:   6082
+  CStrings:  1085
 
Symbols:
+ +[RemoteConfigurationController convertDyldVersionToString:]
+ -[ProviderConfiguration configuration]
+ -[RemoteConfigurationController _dyldSourceVersionString]
+ -[RemoteConfigurationController _initializeProviderConfigurationsWithConfiguration:].cold.1
+ -[RemoteConfigurationController _initializeProviderConfigurationsWithConfiguration:].cold.2
+ -[RemoteConfigurationController _setCurrentConfigurationOnInternalQueue:]
+ -[RemoteConfigurationController currentConfiguration]
+ -[RemoteConfigurationController setCurrentConfiguration:]
+ _OBJC_CLASS_$_NSMutableSet
+ __ZL20configurationBaseURLv
+ __ZL23mergeConfigurationArrayP7NSArrayS0_
+ __ZL35mergeConfigurationArrayIfBothNotNilP7NSArrayS0_
+ __ZN7Backend6Google12SSBUtilities18currentCountryCodeEv
+ __ZN7Backend6Google12SSBUtilities18currentCountryCodeEv.cold.1
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
+ __ZZ57-[RemoteConfigurationController _dyldSourceVersionString]E13versionString
+ __ZZ57-[RemoteConfigurationController _dyldSourceVersionString]E4once
+ __ZZN7Backend6GoogleL15apiKeyForGoogleEvE13useTestAPIKey
+ __ZZN7Backend6GoogleL15apiKeyForGoogleEvE4once
+ ___57-[RemoteConfigurationController _dyldSourceVersionString]_block_invoke
+ ___57-[RemoteConfigurationController _dyldSourceVersionString]_block_invoke.cold.1
+ ___57-[RemoteConfigurationController _dyldSourceVersionString]_block_invoke.cold.2
+ ___57-[RemoteConfigurationController _dyldSourceVersionString]_block_invoke.cold.3
+ ___57-[RemoteConfigurationController setCurrentConfiguration:]_block_invoke
+ ____ZN7Backend6Google12SSBUtilities24shouldConsultWithTencentEv_block_invoke_3
+ ____ZN7Backend6GoogleL15apiKeyForGoogleEv_block_invoke
+ ___block_literal_global.14
+ ___block_literal_global.17
+ ___block_literal_global.20
+ _configurationsKey
+ _dyld_image_header_containing_address
+ _maxVersionKey
+ _minVersionKey
+ _objc_msgSend$_dyldSourceVersionString
+ _objc_msgSend$_setCurrentConfigurationOnInternalQueue:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$allObjects
+ _objc_msgSend$compare:options:
+ _objc_msgSend$convertDyldVersionToString:
+ _objc_msgSend$doubleValue
+ _objc_msgSend$sortedArrayUsingSelector:
+ _versionRangesKey
- -[ProviderConfiguration _currentRegionCode]
- -[RemoteConfigurationController _setCurrentConfiguration:]
- _OBJC_CLASS_$_NSLocale
- _OBJC_CLASS_$_NSProcessInfo
- ____ZN7Backend6Google12SSBUtilities24shouldConsultWithTencentEv_block_invoke.26
- ____ZN7Backend6Google12SSBUtilities24shouldConsultWithTencentEv_block_invoke_2.cold.1
- ___block_literal_global.11
- ___block_literal_global.8
- _objc_msgSend$_currentRegionCode
- _objc_msgSend$_providerToTurnOffFromProviderDictionary:
- _objc_msgSend$_setCurrentConfiguration:
- _objc_msgSend$countryCode
- _objc_msgSend$currentLocale
- _objc_msgSend$numberWithInteger:
- _objc_msgSend$operatingSystemVersion
- _objc_msgSend$processInfo
CStrings:
+ "\x02\x14"
+ "%i.%i.%i"
+ "/AppleInternal/Library/BuildRoots/afcf22e0-3f28-11ef-a8ec-4a8302371c27/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/include/c++/v1/__algorithm/sift_down.h"
+ "/AppleInternal/Library/BuildRoots/afcf22e0-3f28-11ef-a8ec-4a8302371c27/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h"
+ "/AppleInternal/Library/BuildRoots/afcf22e0-3f28-11ef-a8ec-4a8302371c27/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/include/c++/v1/__coroutine/coroutine_handle.h"
+ "/AppleInternal/Library/BuildRoots/afcf22e0-3f28-11ef-a8ec-4a8302371c27/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/include/c++/v1/__functional/function.h"
+ "/AppleInternal/Library/BuildRoots/afcf22e0-3f28-11ef-a8ec-4a8302371c27/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/include/c++/v1/__hash_table"
+ "/AppleInternal/Library/BuildRoots/afcf22e0-3f28-11ef-a8ec-4a8302371c27/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h"
+ "/AppleInternal/Library/BuildRoots/afcf22e0-3f28-11ef-a8ec-4a8302371c27/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/include/c++/v1/__string/char_traits.h"
+ "/AppleInternal/Library/BuildRoots/afcf22e0-3f28-11ef-a8ec-4a8302371c27/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/include/c++/v1/__tree"
+ "/AppleInternal/Library/BuildRoots/afcf22e0-3f28-11ef-a8ec-4a8302371c27/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/include/c++/v1/__utility/exception_guard.h"
+ "/AppleInternal/Library/BuildRoots/afcf22e0-3f28-11ef-a8ec-4a8302371c27/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/include/c++/v1/array"
+ "/AppleInternal/Library/BuildRoots/afcf22e0-3f28-11ef-a8ec-4a8302371c27/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/include/c++/v1/list"
+ "/AppleInternal/Library/BuildRoots/afcf22e0-3f28-11ef-a8ec-4a8302371c27/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/include/c++/v1/optional"
+ "/AppleInternal/Library/BuildRoots/afcf22e0-3f28-11ef-a8ec-4a8302371c27/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/include/c++/v1/span"
+ "/AppleInternal/Library/BuildRoots/afcf22e0-3f28-11ef-a8ec-4a8302371c27/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/include/c++/v1/string"
+ "/AppleInternal/Library/BuildRoots/afcf22e0-3f28-11ef-a8ec-4a8302371c27/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/include/c++/v1/string_view"
+ "/AppleInternal/Library/BuildRoots/afcf22e0-3f28-11ef-a8ec-4a8302371c27/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/include/c++/v1/vector"
+ "AIzaSyDpdAf08lCB2h18kkhS4_j1xrHKgayn0R4"
+ "Configurations"
+ "Could not find LC_SOURCE_VERSION Mach-O command"
+ "DebugSafeBrowsingShouldUseTestAPIKeyForGoogle"
+ "DebugSafeBrowsingShouldUseTestConfigurationURL"
+ "DebugSafeBrowsingTestUpdateInterval"
+ "Mach-O header has incorrect magic: %04x"
+ "Mach-O header not found"
+ "MaxVersion"
+ "MinVersion"
+ "SafeBrowsingRemoteConfiguration-1"
+ "Skipped an entry in the configuration. Expected a NSDictionary, got %{public}@"
+ "Skipped an version range in the configuration. Expected a NSDictionary, got %{public}@"
+ "Skipped an version range in the configuration. Missing min or max versions entries in dictionary"
+ "T@\"NSDictionary\",C,N,V_currentConfiguration"
+ "T@\"NSDictionary\",R,C,N,V_configuration"
+ "Unable to determine SafariSafeBrowsing's version"
+ "Using Google Test API Key"
+ "VersionRanges"
+ "_dyldSourceVersionString"
+ "_setCurrentConfigurationOnInternalQueue:"
+ "addObjectsFromArray:"
+ "allObjects"
+ "compare:"
+ "compare:options:"
+ "convertDyldVersionToString:"
+ "currentConfiguration"
+ "doubleValue"
+ "https://test-safari.apple.com/safebrowsing/"
+ "setCurrentConfiguration:"
+ "sortedArrayUsingSelector:"
- "\x03\x13"
- "%@.%@.%@"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/__algorithm/sift_down.h"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/__coroutine/coroutine_handle.h"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/__functional/function.h"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/__hash_table"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/__string/char_traits.h"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/__tree"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/__utility/exception_guard.h"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/array"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/list"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/optional"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/span"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/string"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/string_view"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/vector"
- "SafeBrowsingRemoteConfiguration-0"
- "_currentRegionCode"
- "_setCurrentConfiguration:"
- "countryCode"
- "currentLocale"
- "numberWithInteger:"
- "operatingSystemVersion"
- "processInfo"

```

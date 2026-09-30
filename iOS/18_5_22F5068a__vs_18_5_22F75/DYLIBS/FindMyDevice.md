## FindMyDevice

> `/System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice`

```diff

 438.35.2.11.19
-  __TEXT.__text: 0x1e030
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_methlist: 0x2404
-  __TEXT.__const: 0xb0
-  __TEXT.__oslogstring: 0x22cc
-  __TEXT.__cstring: 0x3d8f
+  __TEXT.__text: 0x1ff38
+  __TEXT.__auth_stubs: 0x460
+  __TEXT.__objc_methlist: 0x2584
+  __TEXT.__const: 0xb8
+  __TEXT.__oslogstring: 0x2697
+  __TEXT.__cstring: 0x3f69
   __TEXT.__gcc_except_tab: 0x2d4
-  __TEXT.__unwind_info: 0x730
-  __TEXT.__objc_classname: 0x5c3
-  __TEXT.__objc_methname: 0x483d
-  __TEXT.__objc_methtype: 0x112a
-  __TEXT.__objc_stubs: 0x3100
-  __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0x1150
-  __DATA_CONST.__objc_classlist: 0x120
+  __TEXT.__unwind_info: 0x788
+  __TEXT.__objc_classname: 0x619
+  __TEXT.__objc_methname: 0x4cd1
+  __TEXT.__objc_methtype: 0x1153
+  __TEXT.__objc_stubs: 0x34c0
+  __DATA_CONST.__got: 0x178
+  __DATA_CONST.__const: 0x1190
+  __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0xa8
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10a0
-  __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x100
-  __AUTH_CONST.__auth_got: 0x238
-  __AUTH_CONST.__const: 0x4c0
-  __AUTH_CONST.__cfstring: 0x3720
-  __AUTH_CONST.__objc_const: 0x6d10
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x1f0
-  __DATA.__data: 0x910
-  __DATA.__bss: 0x120
+  __DATA_CONST.__objc_selrefs: 0x11c0
+  __DATA_CONST.__objc_protorefs: 0x68
+  __DATA_CONST.__objc_superrefs: 0x108
+  __AUTH_CONST.__auth_got: 0x240
+  __AUTH_CONST.__const: 0x4e0
+  __AUTH_CONST.__cfstring: 0x3a20
+  __AUTH_CONST.__objc_const: 0x6f80
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0x200
+  __DATA.__data: 0x970
+  __DATA.__bss: 0x128
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xa00
-  __DATA_DIRTY.__bss: 0x40
+  __DATA_DIRTY.__bss: 0x48
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 900
-  Symbols:   3623
-  CStrings:  1759
+  Functions: 949
+  Symbols:   3795
+  CStrings:  1854
 
Symbols:
+ +[FMDSharedConfiguration localizedStringWithKey:]
+ +[FMDSharedConfiguration sharedInstance]
+ +[FMDSharedConfiguration sharedInstance].cold.1
+ +[FMNSXPCConnectionConfiguration sharedConfigurationConfiguration]
+ -[FMDSharedConfiguration contentsWithLocale:]
+ -[FMDSharedConfiguration defaultEntryForConfiguration:deviceClasses:]
+ -[FMDSharedConfiguration downloadWithLocale:reply:]
+ -[FMDSharedConfiguration downloadWithReply:]
+ -[FMDSharedConfiguration entryForConfiguration:deviceClasses:]
+ -[FMDSharedConfiguration entryForConfiguration:deviceClasses:locale:]
+ -[FMDSharedConfiguration entryWithData:key:deviceClasses:]
+ -[FMDSharedConfiguration entryWithData:key:deviceClasses:].cold.1
+ -[FMDSharedConfiguration entryWithData:key:deviceClasses:].cold.10
+ -[FMDSharedConfiguration entryWithData:key:deviceClasses:].cold.11
+ -[FMDSharedConfiguration entryWithData:key:deviceClasses:].cold.2
+ -[FMDSharedConfiguration entryWithData:key:deviceClasses:].cold.3
+ -[FMDSharedConfiguration entryWithData:key:deviceClasses:].cold.4
+ -[FMDSharedConfiguration entryWithData:key:deviceClasses:].cold.5
+ -[FMDSharedConfiguration entryWithData:key:deviceClasses:].cold.6
+ -[FMDSharedConfiguration entryWithData:key:deviceClasses:].cold.7
+ -[FMDSharedConfiguration entryWithData:key:deviceClasses:].cold.8
+ -[FMDSharedConfiguration entryWithData:key:deviceClasses:].cold.9
+ -[FMDSharedConfiguration expiryDateWithContents:]
+ -[FMDSharedConfiguration fileURLWithLocale:]
+ -[FMDSharedConfiguration fileURLWithLocale:].cold.1
+ -[FMDSharedConfiguration fileURLWithLocale:].cold.2
+ -[FMDSharedConfiguration getTheftAndLossCoverageWithSerialNumber:reply:]
+ -[FMDSharedConfiguration localeString]
+ -[FMDSharedConfiguration localeString].cold.1
+ -[FMDSharedConfiguration localeString].cold.2
+ -[FMDSharedConfigurationEntry .cxx_destruct]
+ -[FMDSharedConfigurationEntry disclaimer]
+ -[FMDSharedConfigurationEntry init]
+ -[FMDSharedConfigurationEntry isEnabled]
+ -[FMDSharedConfigurationEntry message]
+ -[FMDSharedConfigurationEntry setDisclaimer:]
+ -[FMDSharedConfigurationEntry setEnabled:]
+ -[FMDSharedConfigurationEntry setMessage:]
+ -[FMDSharedConfigurationEntry setTitle:]
+ -[FMDSharedConfigurationEntry title]
+ _FMDSharedConfigurationKeyTheftAndLoss
+ _OBJC_CLASS_$_FMDSharedConfiguration
+ _OBJC_CLASS_$_FMDSharedConfigurationEntry
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_IVAR_$_FMDSharedConfigurationEntry._disclaimer
+ _OBJC_IVAR_$_FMDSharedConfigurationEntry._enabled
+ _OBJC_IVAR_$_FMDSharedConfigurationEntry._message
+ _OBJC_IVAR_$_FMDSharedConfigurationEntry._title
+ _OBJC_METACLASS_$_FMDSharedConfiguration
+ _OBJC_METACLASS_$_FMDSharedConfigurationEntry
+ __OBJC_$_CLASS_METHODS_FMDSharedConfiguration
+ __OBJC_$_CLASS_PROP_LIST_FMDSharedConfiguration
+ __OBJC_$_INSTANCE_METHODS_FMDSharedConfiguration
+ __OBJC_$_INSTANCE_METHODS_FMDSharedConfigurationEntry
+ __OBJC_$_INSTANCE_VARIABLES_FMDSharedConfigurationEntry
+ __OBJC_$_PROP_LIST_FMDSharedConfiguration
+ __OBJC_$_PROP_LIST_FMDSharedConfigurationEntry
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FMDSharedConfigurationXPCInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FMDSharedConfigurationXPCInterface
+ __OBJC_$_PROTOCOL_REFS_FMDSharedConfigurationXPCInterface
+ __OBJC_CLASS_RO_$_FMDSharedConfiguration
+ __OBJC_CLASS_RO_$_FMDSharedConfigurationEntry
+ __OBJC_LABEL_PROTOCOL_$_FMDSharedConfigurationXPCInterface
+ __OBJC_METACLASS_RO_$_FMDSharedConfiguration
+ __OBJC_METACLASS_RO_$_FMDSharedConfigurationEntry
+ __OBJC_PROTOCOL_$_FMDSharedConfigurationXPCInterface
+ __OBJC_PROTOCOL_REFERENCE_$_FMDSharedConfigurationXPCInterface
+ ___40+[FMDSharedConfiguration sharedInstance]_block_invoke
+ ___44-[FMDSharedConfiguration downloadWithReply:]_block_invoke
+ ___51-[FMDSharedConfiguration downloadWithLocale:reply:]_block_invoke
+ ___51-[FMDSharedConfiguration downloadWithLocale:reply:]_block_invoke_2
+ ___72-[FMDSharedConfiguration getTheftAndLossCoverageWithSerialNumber:reply:]_block_invoke
+ ___72-[FMDSharedConfiguration getTheftAndLossCoverageWithSerialNumber:reply:]_block_invoke_2
+ _kFMDBrassStatusKey
+ _kFMDSharedConfigurationAccessEntitlement
+ _kFMDSharedConfigurationConfigVersionKey
+ _kFMDSharedConfigurationDataKey
+ _kFMDSharedConfigurationExpiryKey
+ _kFMDSharedConfigurationLastRequestedKey
+ _kFMDSharedConfigurationXPCServiceAccessEntitlement
+ _objc_msgSend$JSONObjectWithData:options:error:
+ _objc_msgSend$URLByAppendingPathComponent:isDirectory:
+ _objc_msgSend$bundleForClass:
+ _objc_msgSend$compare:
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$containerURLForSecurityApplicationGroupIdentifier:
+ _objc_msgSend$contentsWithLocale:
+ _objc_msgSend$count
+ _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$dateByAddingTimeInterval:
+ _objc_msgSend$defaultEntryForConfiguration:deviceClasses:
+ _objc_msgSend$dictionaryWithContentsOfURL:error:
+ _objc_msgSend$doubleValue
+ _objc_msgSend$downloadSharedConfigurationWithLocale:reply:
+ _objc_msgSend$downloadWithLocale:reply:
+ _objc_msgSend$entryForConfiguration:deviceClasses:locale:
+ _objc_msgSend$entryWithData:key:deviceClasses:
+ _objc_msgSend$expiryDateWithContents:
+ _objc_msgSend$fileURLWithLocale:
+ _objc_msgSend$getTheftAndLossCoverageWithSerialNumber:reply:
+ _objc_msgSend$localeString
+ _objc_msgSend$localizedStringForKey:value:table:
+ _objc_msgSend$localizedStringWithKey:
+ _objc_msgSend$minimizedLanguagesFromLanguages:
+ _objc_msgSend$now
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$preferredLanguages
+ _objc_msgSend$setDisclaimer:
+ _objc_msgSend$setEnabled:
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_release_x28
+ _sharedInstance.dispatch_predicate
CStrings:
+ "%@.plist"
+ ","
+ "Application Support"
+ "Calling process has no preferredLanguages."
+ "Calling process is missing InternationalSupport."
+ "Calling process is missing container entitlements"
+ "DA"
+ "Entry at index %lu doesn't have a category"
+ "Entry at index %lu is not a dictionary"
+ "Entry found at %lu, but disclaimer label exists and is not a string: %@"
+ "Entry found at %lu, but doesn't contain an enabled flag"
+ "Entry found at %lu, but enabled flag isn't a number: %@"
+ "Entry found at %lu, but it doesn't contain a message"
+ "Entry found at %lu, but it doesn't contain a title"
+ "Entry found at %lu, but message is not a string: %@"
+ "Entry found at %lu, but title is not a string: %@"
+ "FMDSharedConfiguration"
+ "FMDSharedConfigurationEntry"
+ "FMDSharedConfigurationXPCInterface"
+ "Failed to create container directories"
+ "Failed to read contents for %@, error: %@"
+ "Has existing shared configuration for '%@' and it has not yet expired (%@)"
+ "JSONObjectWithData:options:error:"
+ "LR"
+ "Library"
+ "Localizable-WARRANTY_DIAGNOSTICS"
+ "No contents for %@"
+ "No data for %@, returning default"
+ "No defaults for configuration %@ (%@)"
+ "No entries"
+ "No entry for %@"
+ "No match found among %lu entries"
+ "Not valid JSON: %@"
+ "T@\"FMDSharedConfiguration\",R,N"
+ "T@\"NSString\",C,N,V_disclaimer"
+ "T@\"NSString\",C,N,V_message"
+ "T@\"NSString\",C,N,V_title"
+ "TB,N,GisEnabled,V_enabled"
+ "TNL_DISCLAIMER_LABEL_DEFAULT"
+ "TNL_DISCLAIMER_MESSAGE_DEFAULT"
+ "TNL_DISCLAIMER_TITLE_DEFAULT"
+ "TTL"
+ "URLByAppendingPathComponent:isDirectory:"
+ "Unsupported top-level type: %@"
+ "V"
+ "_disclaimer"
+ "_enabled"
+ "awarenessEnabled"
+ "awarenessStrings"
+ "brassStatus"
+ "bundleForClass:"
+ "category"
+ "com.apple.icloud.FindMyDevice.FindMyDeviceSharedConfiguration.access"
+ "com.apple.icloud.FindMyDevice.FindMyDeviceSharedConfigurationXPCService.access"
+ "compare:"
+ "componentsJoinedByString:"
+ "containerURLForSecurityApplicationGroupIdentifier:"
+ "contentsWithLocale:"
+ "count"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "dateByAddingTimeInterval:"
+ "defaultEntryForConfiguration:deviceClasses:"
+ "dictionaryWithContentsOfURL:error:"
+ "disclaimer"
+ "disclaimerLabel"
+ "doubleValue"
+ "downloadSharedConfigurationWithLocale:reply:"
+ "downloadWithLocale:reply:"
+ "downloadWithReply:"
+ "en-US"
+ "enabled"
+ "entryForConfiguration:deviceClasses:"
+ "entryForConfiguration:deviceClasses:locale:"
+ "entryWithData:key:deviceClasses:"
+ "expiryDateWithContents:"
+ "fileURLWithLocale:"
+ "getTheftAndLossCoverageWithSerialNumber:reply:"
+ "getTheftAndLossCoverageWithUDID:reply:"
+ "group.com.apple.icloud.findmydevice.shared-configuration"
+ "iPhone"
+ "isEnabled"
+ "localeString"
+ "localizedStringForKey:value:table:"
+ "localizedStringWithKey:"
+ "minimizedLanguagesFromLanguages:"
+ "now"
+ "objectAtIndexedSubscript:"
+ "preferredLanguages"
+ "setDisclaimer:"
+ "setEnabled:"
+ "sharedConfigurationConfiguration"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "theftLoss"
+ "v32@0:8@\"NSString\"16@?<v@?Q@\"NSError\">24"
+ "~"

```

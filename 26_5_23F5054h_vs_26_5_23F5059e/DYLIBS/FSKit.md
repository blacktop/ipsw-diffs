## FSKit

> `/System/Library/PrivateFrameworks/FSKit.framework/FSKit`

```diff

-737.120.8.0.0
-  __TEXT.__text: 0x42d24
+737.120.9.0.0
+  __TEXT.__text: 0x42c80
   __TEXT.__auth_stubs: 0xd70
-  __TEXT.__objc_methlist: 0x4e9c
+  __TEXT.__objc_methlist: 0x4e6c
   __TEXT.__const: 0x3f8
-  __TEXT.__gcc_except_tab: 0xdd8
+  __TEXT.__gcc_except_tab: 0xde8
   __TEXT.__oslogstring: 0x3213
-  __TEXT.__cstring: 0x45af
+  __TEXT.__cstring: 0x456f
   __TEXT.__swift5_typeref: 0x1d1
   __TEXT.__swift5_capture: 0x58
   __TEXT.__swift5_reflstr: 0x16

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x1378
+  __TEXT.__unwind_info: 0x1368
   __TEXT.__eh_frame: 0x1b0
   __TEXT.__objc_classname: 0x9bd
-  __TEXT.__objc_methname: 0x9d8a
-  __TEXT.__objc_methtype: 0x3055
-  __TEXT.__objc_stubs: 0x5b20
+  __TEXT.__objc_methname: 0x9c5e
+  __TEXT.__objc_methtype: 0x3035
+  __TEXT.__objc_stubs: 0x5a20
   __DATA_CONST.__got: 0x3f8
   __DATA_CONST.__const: 0x1350
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x25b0
+  __DATA_CONST.__objc_selrefs: 0x2550
   __DATA_CONST.__objc_protorefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x2d8
   __AUTH_CONST.__auth_got: 0x6c8
   __AUTH_CONST.__const: 0x508
-  __AUTH_CONST.__cfstring: 0x26a0
-  __AUTH_CONST.__objc_const: 0x8590
+  __AUTH_CONST.__cfstring: 0x2660
+  __AUTH_CONST.__objc_const: 0x8540
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x2a8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x10e0
   __AUTH.__data: 0x80
-  __DATA.__objc_ivar: 0x4e8
+  __DATA.__objc_ivar: 0x4e0
   __DATA.__data: 0xef8
   __DATA.__bss: 0x320
   __DATA_DIRTY.__objc_data: 0x910

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 20F2EC29-52A1-3D0D-A35E-0AA3E88AC57B
-  Functions: 2135
-  Symbols:   6803
-  CStrings:  3478
+  UUID: 3D6766F6-42D0-39F4-98E9-38C1F67C158C
+  Functions: 2131
+  Symbols:   6785
+  CStrings:  3456
 
Symbols:
+ -[FSModuleHost(Project) moduleInstanceForExtensionIdentity:]
+ -[FSModuleHost(Project) updateProviderListForMatchingExtensionRecords:]
+ -[FSModuleIdentity bundleIDIsSystem:]
+ -[FSModuleIdentity initWithExtensionIdentity:isEnabled:isSystem:]
+ -[FSModuleIdentity(Project) initWithExtensionIdentity:isEnabled:]
+ -[FSModuleInstance exIdentity]
+ -[FSModuleInstance(Project) initWithExtensionIdentity:]
+ -[FSModuleInstance(Project) initWithExtensionIdentity:enabled:]
+ GCC_except_table38
+ GCC_except_table41
+ _OBJC_CLASS_$_NSCondition
+ _OBJC_IVAR_$_FSModuleInstance._exIdentity
+ __OBJC_$_INSTANCE_METHODS_FSModuleIdentity(Private|Project)
+ __OBJC_$_INSTANCE_METHODS_FSModuleInstance(Project)
+ ___46-[FSModuleHost(Project) extensionPointRecords]_block_invoke.149
+ ___73-[FSModuleHost(Project) _updateProviderListForFilteredFSModuleInstances:]_block_invoke.187
+ ___73-[FSModuleHost(Project) _updateProviderListForFilteredFSModuleInstances:]_block_invoke_2.189
+ ___block_literal_global.152
+ ___block_literal_global.159
+ ___block_literal_global.181
+ ___block_literal_global.183
+ _objc_msgSend$bundleIDIsSystem:
+ _objc_msgSend$exIdentity
+ _objc_msgSend$initWithExtensionIdentity:enabled:
+ _objc_msgSend$initWithExtensionIdentity:isEnabled:
+ _objc_msgSend$initWithExtensionIdentity:isEnabled:isSystem:
+ _objc_msgSend$mainBundle
- -[FSModuleIdentity applicationGroup]
- -[FSModuleIdentity initWithApplicationExtensionRecord:isEnabled:]
- -[FSModuleIdentity initWithApplicationExtensionRecord:isEnabled:isSystem:]
- -[FSModuleInstance containingURL]
- -[FSModuleInstance entitlementNamed:ofClass:]
- -[FSModuleInstance entitlements]
- -[FSModuleInstance executableURL]
- -[FSModuleInstance extensionDictionary]
- -[FSModuleInstance extensionPointIdentifier]
- -[FSModuleInstance platform]
- -[FSModuleInstance record]
- -[FSModuleInstance sdkDictionary]
- GCC_except_table37
- _OBJC_CLASS_$_LSBundleRecord
- _OBJC_IVAR_$_FSModuleIdentity._applicationGroup
- _OBJC_IVAR_$_FSModuleInstance._executableURL
- _OBJC_IVAR_$_FSModuleInstance._record
- __OBJC_$_INSTANCE_METHODS_FSModuleIdentity
- __OBJC_$_INSTANCE_METHODS_FSModuleInstance
- __OBJC_$_PROP_LIST_FSModuleIdentity
- ___46-[FSModuleHost(Project) extensionPointRecords]_block_invoke.148
- ___73-[FSModuleHost(Project) _updateProviderListForFilteredFSModuleInstances:]_block_invoke.186
- ___73-[FSModuleHost(Project) _updateProviderListForFilteredFSModuleInstances:]_block_invoke_2.188
- ___block_literal_global.151
- ___block_literal_global.158
- ___block_literal_global.180
- ___block_literal_global.182
- _objc_msgSend$SDKDictionary
- _objc_msgSend$URL
- _objc_msgSend$_expensiveDictionaryRepresentation
- _objc_msgSend$applicationExtensionRecord
- _objc_msgSend$bundleRecordForCurrentProcess
- _objc_msgSend$containingBundleRecord
- _objc_msgSend$entitlements
- _objc_msgSend$extensionPointRecord
- _objc_msgSend$infoDictionary
- _objc_msgSend$initWithApplicationExtensionRecord:isEnabled:
- _objc_msgSend$initWithApplicationExtensionRecord:isEnabled:isSystem:
- _objc_msgSend$objectForKey:ofClass:
- _objc_msgSend$platform
- _objc_msgSend$record
CStrings:
+ "0000000000"
+ "@\"_EXExtensionIdentity\""
+ "Extension identity [%@]: %@"
+ "FSModuleHost callback queue"
+ "T@\"NSDictionary\",R"
+ "T@\"NSURL\",R"
+ "T@\"_EXExtensionIdentity\",R,N,V_exIdentity"
+ "TB,N,GisEnabled,SsetEnabled:"
+ "TB,R,GisSystem"
+ "_exIdentity"
+ "bundleIDIsSystem:"
+ "exIdentity"
+ "initWithExtensionIdentity:enabled:"
+ "initWithExtensionIdentity:isEnabled:"
+ "initWithExtensionIdentity:isEnabled:isSystem:"
+ "mainBundle"
+ "moduleInstanceForExtensionIdentity:"
+ "updateProviderListForMatchingExtensionRecords:"
- "@\"LSApplicationExtensionRecord\""
- "@32@0:8@16#24"
- "Application-Group"
- "EXAppExtensionAttributes"
- "Extension identity [%@]: %@ platform: %u"
- "FPDExtensionManager callback queue"
- "NSExtension"
- "SDKDictionary"
- "T@\"LSApplicationExtensionRecord\",R,N,V_record"
- "T@\"NSDictionary\",R,D"
- "T@\"NSString\",R,D"
- "T@\"NSString\",R,V_applicationGroup"
- "T@\"NSURL\",R,D"
- "T@\"NSURL\",R,V_executableURL"
- "T@\"NSUUID\",R,D"
- "TI,R,D"
- "_applicationGroup"
- "_executableURL"
- "_expensiveDictionaryRepresentation"
- "_record"
- "applicationExtensionRecord"
- "applicationGroup"
- "bundleRecordForCurrentProcess"
- "containingBundleRecord"
- "containingURL"
- "entitlementNamed:ofClass:"
- "entitlements"
- "executableURL"
- "extensionDictionary"
- "extensionPointIdentifier"
- "extensionPointRecord"
- "infoDictionary"
- "initWithApplicationExtensionRecord:isEnabled:"
- "initWithApplicationExtensionRecord:isEnabled:isSystem:"
- "objectForKey:ofClass:"
- "platform"
- "record"
- "sdkDictionary"

```

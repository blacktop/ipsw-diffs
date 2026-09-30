## PackageKit

> `/System/Library/PrivateFrameworks/PackageKit.framework/Versions/A/PackageKit`

```diff

-1443.0.0.0.0
-  __TEXT.__text: 0x82c98
-  __TEXT.__auth_stubs: 0x1df0
-  __TEXT.__objc_methlist: 0x70bc
-  __TEXT.__const: 0x258
-  __TEXT.__cstring: 0x10ddd
+1446.0.0.0.0
+  __TEXT.__text: 0x8448c
+  __TEXT.__auth_stubs: 0x1fd0
+  __TEXT.__objc_methlist: 0x7124
+  __TEXT.__cstring: 0x110ca
+  __TEXT.__const: 0x308
+  __TEXT.__constg_swiftt: 0x188
+  __TEXT.__swift5_typeref: 0x7c
+  __TEXT.__swift5_reflstr: 0x21
+  __TEXT.__swift5_fieldmd: 0x5c
+  __TEXT.__swift5_types: 0x8
   __TEXT.__gcc_except_tab: 0x11a8
   __TEXT.__oslogstring: 0x19
   __TEXT.__dof_PackageKi: 0x1b03
-  __TEXT.__unwind_info: 0x1f88
+  __TEXT.__unwind_info: 0x2000
   __TEXT.__eh_frame: 0x40
   __TEXT.__objc_classname: 0x1074
-  __TEXT.__objc_methname: 0x117fe
-  __TEXT.__objc_methtype: 0x23e6
-  __TEXT.__objc_stubs: 0xdc00
-  __DATA_CONST.__got: 0x970
-  __DATA_CONST.__const: 0xb70
-  __DATA_CONST.__objc_classlist: 0x438
+  __TEXT.__objc_methname: 0x11877
+  __TEXT.__objc_methtype: 0x242a
+  __TEXT.__objc_stubs: 0xdc80
+  __DATA_CONST.__got: 0x9a0
+  __DATA_CONST.__const: 0xba8
+  __DATA_CONST.__objc_classlist: 0x440
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4350
+  __DATA_CONST.__objc_selrefs: 0x4378
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x3a0
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0xf08
-  __AUTH_CONST.__const: 0x15f0
-  __AUTH_CONST.__cfstring: 0xb420
-  __AUTH_CONST.__objc_const: 0xc178
+  __AUTH_CONST.__auth_got: 0xff8
+  __AUTH_CONST.__auth_ptr: 0x18
+  __AUTH_CONST.__const: 0x1760
+  __AUTH_CONST.__cfstring: 0xb440
+  __AUTH_CONST.__objc_const: 0xc298
   __AUTH_CONST.__objc_intobj: 0x408
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0x2a30
+  __AUTH.__objc_data: 0x2aa0
+  __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x9d0
-  __DATA.__data: 0x810
+  __DATA.__data: 0x830
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x128
+  __DATA.__bss: 0x230
   __DATA.__common: 0x8
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxar.1.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2741
-  Symbols:   7322
-  CStrings:  2026
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  Functions: 2771
+  Symbols:   7390
+  CStrings:  2045
 
Symbols:
+ +[PKInstallScriptOverrides _loadPlistNamed:rootClass:]
+ +[PKInstallScriptOverrides _parseTrieFromDictionary:key:]
+ -[PKInstallScriptAction initWithScriptRelativePath:componentPackageIdentifierExpressions:performMutation:dropSIP:skip:relativePathTransformation:]
+ -[PKInstallScriptMutation initWithScriptPath:dropSIP:skipScript:mutationToPerform:]
+ OBJC_IVAR_$_PKInstallScriptOverrides._packageIdentifiersDroppingSIP
+ _OBJC_CLASS_$_PKTrie
+ _OBJC_METACLASS_$_PKTrie
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __DATA_PKTrie
+ __INSTANCE_METHODS_PKTrie
+ __IVARS_PKTrie
+ __IVARS__TtC10PackageKit4Trie
+ __IVARS__TtC10PackageKitP33_7D30894BCA118536701CB529A15A107F8TrieNode
+ __METACLASS_DATA_PKTrie
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_instantiateGenericMetadata
+ ___swift_reflection_version
+ ___unnamed_1
+ ___unnamed_6
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_PackageKit
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_PackageKit
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_PackageKit
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_PackageKit
+ __swift_FORCE_LOAD_$_swiftIOKit
+ __swift_FORCE_LOAD_$_swiftIOKit_$_PackageKit
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_PackageKit
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_PackageKit
+ _memmove
+ _objc_msgSend$_loadPlistNamed:rootClass:
+ _objc_msgSend$_parseTrieFromDictionary:key:
+ _objc_msgSend$addString:
+ _objc_msgSend$containsStringPrefixing:
+ _swift_allocObject
+ _swift_allocateGenericClassMetadata
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_deallocClassInstance
+ _swift_endAccess
+ _swift_getGenericMetadata
+ _swift_getObjCClassMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_initClassMetadata2
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release
+ _swift_retain
+ _swift_weakAssign
+ _swift_weakDestroy
+ _swift_weakInit
+ _symbolic 7ElementSTQz
+ _symbolic SDyx_____yxGG 10PackageKit8TrieNode33_7D30894BCA118536701CB529A15A107FLLC
+ _symbolic Sb
+ _symbolic _____ 10PackageKit4TrieC
+ _symbolic _____ 10PackageKit8TrieNode33_7D30894BCA118536701CB529A15A107FLLC
+ _symbolic _____y7ElementSTQzG 10PackageKit8TrieNode33_7D30894BCA118536701CB529A15A107FLLC
+ _symbolic _____ySJG 10PackageKit8TrieNode33_7D30894BCA118536701CB529A15A107FLLC
+ _symbolic _____ySJ_____ySJGG s18_DictionaryStorageC 10PackageKit8TrieNode33_7D30894BCA118536701CB529A15A107FLLC
+ _symbolic _____ySSG 10PackageKit4TrieC
+ _symbolic _____yxGSgXw 10PackageKit8TrieNode33_7D30894BCA118536701CB529A15A107FLLC
+ _symbolic x
+ _symbolic xSg
- -[PKInstallScriptAction initWithScriptRelativePath:scriptTypes:componentPackageIdentifierExpressions:performMutation:dropSIP:skip:relativePathTransformation:]
- OBJC_IVAR_$_PKInstallScriptAction._scriptTypes
CStrings:
+ "+[PKInstallScriptOverrides _loadPlistNamed:rootClass:] was invoked with an unsupported root class."
+ "@16@0:8"
+ "B24@0:8@16"
+ "BUG IN PackageKit: +[PKInstallScriptOverrides _loadPlistNamed:rootClass:] was invoked with an unsupported root class."
+ "BUG IN PackageKit: Failed to deserialize plist array for PKInstallScriptOverrides"
+ "BUG IN PackageKit: Failed to deserialize plist dictionary for PKInstallScriptOverrides"
+ "BUG IN PackageKit: Failed to load plist for PKInstallScriptOverrides."
+ "BUG IN PackageKit: InstallScriptTries contains a key that is not a valid array."
+ "Failed to deserialize plist array for PKInstallScriptOverrides"
+ "Failed to deserialize plist dictionary for PKInstallScriptOverrides"
+ "Failed to load plist for PKInstallScriptOverrides."
+ "InstallScriptTries"
+ "InstallScriptTries contains a key that is not a valid array."
+ "PKTrie"
+ "PackageKit: A script mutation for path (%!s(MISSING)) is dropping rootful permissions."
+ "PackageKit: A script mutation for path (%!s(MISSING)) is skipping the script."
+ "PackageKit: FATAL-- Failed to deserialize %!s(MISSING) as a dictionary at path:(%!s(MISSING)). %!s(MISSING)"
+ "PackageKit: FATAL-- Failed to deserialize %!s(MISSING) as an array at path:(%!s(MISSING)). %!s(MISSING)"
+ "PackageKit: FATAL-- Failed to load %!s(MISSING) within bundle:(%!s(MISSING))."
+ "PackageKit: InstallScriptTries for key:(%!s(MISSING)) contains an identifier that is not a string. Skipping..."
+ "PackageKit: InstallScriptTries for key:(%!s(MISSING)) is not an array."
+ "match"
+ "parent"
+ "trie"
+ "v16@0:8"
+ "v24@0:8@16"
+ "value"
- "BUG IN PackageKit: Failed to deserialize InstallScriptActions for PKInstallScriptOverrides"
- "BUG IN PackageKit: Failed to load InstallScriptActions for PKInstallScriptOverrides."
- "Failed to deserialize InstallScriptActions for PKInstallScriptOverrides"
- "Failed to load InstallScriptActions for PKInstallScriptOverrides."
- "PackageKit: A script mutation for path (%!s(MISSING)) has requested to drop rootful permissions."
- "PackageKit: A script mutation for path (%!s(MISSING)) has requested to skip the script."
- "PackageKit: FATAL-- Failed to deserialize InstallScriptActions at path:(%!s(MISSING)). %!s(MISSING)"
- "PackageKit: FATAL-- Failed to load InstallScriptActions within bundle:(%!s(MISSING))."

```

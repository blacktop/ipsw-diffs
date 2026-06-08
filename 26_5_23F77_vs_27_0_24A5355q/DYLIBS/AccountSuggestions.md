## AccountSuggestions

> `/System/Library/PrivateFrameworks/AccountSuggestions.framework/AccountSuggestions`

```diff

-98.0.0.0.0
-  __TEXT.__text: 0x1b1b8
-  __TEXT.__auth_stubs: 0xac0
+110.0.0.0.0
+  __TEXT.__text: 0x1af74
   __TEXT.__objc_methlist: 0x20
-  __TEXT.__const: 0x6aa
-  __TEXT.__swift5_typeref: 0x2f1
+  __TEXT.__const: 0x69a
+  __TEXT.__swift5_typeref: 0x2cf
   __TEXT.__cstring: 0x143
   __TEXT.__swift5_capture: 0xe8
   __TEXT.__oslogstring: 0x479

   __TEXT.__swift5_proto: 0x30
   __TEXT.__swift5_types: 0x18
   __TEXT.__unwind_info: 0x4b0
-  __TEXT.__eh_frame: 0x448
-  __TEXT.__objc_classname: 0x33
-  __TEXT.__objc_methname: 0x43e
-  __TEXT.__objc_methtype: 0x1a
-  __TEXT.__objc_stubs: 0x480
-  __DATA_CONST.__got: 0x280
-  __DATA_CONST.__const: 0xe0
+  __TEXT.__eh_frame: 0x3f0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x130
-  __AUTH_CONST.__auth_got: 0x568
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x618
   __AUTH_CONST.__objc_const: 0x210
-  __DATA.__data: 0x70
-  __DATA.__bss: 0x520
+  __AUTH_CONST.__auth_got: 0x620
+  __DATA.__data: 0x50
+  __DATA.__bss: 0x4a0
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0x5a0
-  __DATA_DIRTY.__bss: 0x100
+  __DATA_DIRTY.__data: 0x5b0
+  __DATA_DIRTY.__bss: 0x180
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: A31E2166-BD6C-3C4F-8791-FD9C5E5BAD47
-  Functions: 452
-  Symbols:   380
-  CStrings:  90
+  UUID: DA749EF7-C6AE-3021-A5AB-0CFA662F1077
+  Functions: 455
+  Symbols:   425
+  CStrings:  34
 
Symbols:
+ ___swift_closure_destructor
+ ___swift_closure_destructor.101
+ ___swift_closure_destructor.104
+ ___swift_closure_destructor.107
+ ___swift_closure_destructor.16
+ ___swift_closure_destructor.25
+ ___swift_closure_destructor.34
+ ___swift_closure_destructor.34Tm
+ ___swift_closure_destructor.40
+ ___swift_closure_destructor.46
+ ___swift_closure_destructor.86
+ ___swift_closure_destructor.86Tm
+ ___swift_closure_destructor.92
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_AccountSuggestions
+ _objc_retain_x26
+ _swift_release_n
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x3
+ _swift_release_x8
+ _swift_release_x9
+ _swift_retain_x1
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_retain_x26
+ _symbolic SS3key_yp5valuet
- _objectdestroy.34Tm
- _objectdestroy.86Tm
- _swift_stdlib_isStackAllocationSafe
- _symbolic SS3key______5valuetSg 10Foundation4DateV
- _symbolic SS3key______5valuetSg 18AccountSuggestions0A10SuggestionV
- _symbolic ______p s5ErrorP
CStrings:
- "_TtC18AccountSuggestions24AccountSuggestionManager"
- "_allSuggestions"
- "_filteredSuggestions"
- "aa_isAccountClass:"
- "accountProperties"
- "accountPropertyForKey:"
- "accountType"
- "accountTypesThatNeedProperties"
- "accountWithIdentifier:"
- "accountsWithAccountTypeIdentifiers:error:"
- "addObserver:selector:name:object:"
- "animationWrapperBlock"
- "boolForKey:"
- "defaultCenter"
- "defaultStore"
- "defaults"
- "deviceLastUsedDates"
- "dictionaryForKey:"
- "dictionaryRepresentation"
- "dirtyAccountProperties"
- "dirtyProperties"
- "doubleForKey:"
- "identifier"
- "initWithAccountType:"
- "initWithDictionary:"
- "initWithStoreIdentifier:type:"
- "initWithSuiteName:"
- "isDataSeparatedAccount"
- "isEqual:"
- "isEqualToDictionary:"
- "kvs"
- "kvsSubscriber"
- "locallySupportedAccountTypes"
- "nonUpdatingMode"
- "objectForKeyedSubscript:"
- "parentAccount"
- "personaIdentifier"
- "previousWorkItem"
- "reloadAccounts"
- "reloadDelay:"
- "removeObjectForKey:"
- "removeObserver:name:object:"
- "setAccountProperty:forKey:"
- "setBool:forKey:"
- "setDictionary:forKey:"
- "setObject:forKey:"
- "setUsername:"
- "stringForKey:"
- "suggestionsByID"
- "supportedAccountTypes"
- "synchronize"
- "username"
- "v16@0:8"
- "v24@0:8@16"
- "v8@?0"
- "workQueue"

```

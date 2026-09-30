## UserNotificationsCore

> `/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-713.0.0.0.0
-  __TEXT.__text: 0x231938
+717.0.0.0.0
+  __TEXT.__text: 0x236050
   __TEXT.__objc_methlist: 0x5f74
-  __TEXT.__const: 0x1363c
-  __TEXT.__cstring: 0x90d1
-  __TEXT.__oslogstring: 0x1160a
+  __TEXT.__const: 0x1365c
+  __TEXT.__cstring: 0x9191
+  __TEXT.__oslogstring: 0x118aa
   __TEXT.__gcc_except_tab: 0x448
   __TEXT.__dlopen_cstrs: 0x60
   __TEXT.__constg_swiftt: 0x7960
   __TEXT.__swift5_typeref: 0x77d7
-  __TEXT.__swift5_reflstr: 0x474a
-  __TEXT.__swift5_fieldmd: 0x5164
+  __TEXT.__swift5_reflstr: 0x47ea
+  __TEXT.__swift5_fieldmd: 0x5194
   __TEXT.__swift5_builtin: 0x1f4
   __TEXT.__swift5_assocty: 0x708
   __TEXT.__swift5_proto: 0xd78
   __TEXT.__swift5_types: 0x5e0
   __TEXT.__swift5_protos: 0x180
   __TEXT.__swift5_capture: 0x20f8
-  __TEXT.__swift_as_entry: 0x214
-  __TEXT.__swift_as_ret: 0x238
-  __TEXT.__swift_as_cont: 0x3e4
+  __TEXT.__swift_as_entry: 0x220
+  __TEXT.__swift_as_ret: 0x24c
+  __TEXT.__swift_as_cont: 0x408
   __TEXT.__swift5_mpenum: 0x6c
-  __TEXT.__unwind_info: 0x64c0
-  __TEXT.__eh_frame: 0x82d4
+  __TEXT.__unwind_info: 0x6550
+  __TEXT.__eh_frame: 0x85d4
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x2f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3e10
+  __DATA_CONST.__objc_selrefs: 0x3e70
   __DATA_CONST.__objc_protorefs: 0x170
   __DATA_CONST.__objc_superrefs: 0x180
-  __DATA_CONST.__got: 0x1720
+  __DATA_CONST.__got: 0x1738
   __AUTH_CONST.__const: 0xd9b8
   __AUTH_CONST.__cfstring: 0x48a0
   __AUTH_CONST.__objc_const: 0x23810
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH_CONST.__auth_got: 0x2310
+  __AUTH_CONST.__auth_got: 0x2320
   __AUTH.__objc_data: 0x1108
   __AUTH.__data: 0x34c8
   __DATA.__objc_ivar: 0x704
-  __DATA.__data: 0x4098
+  __DATA.__data: 0x40a8
   __DATA.__bss: 0xf480
   __DATA.__common: 0x1b0
   __DATA_DIRTY.__objc_data: 0x2808
-  __DATA_DIRTY.__data: 0x72f0
+  __DATA_DIRTY.__data: 0x7340
   __DATA_DIRTY.__bss: 0x7930
   __DATA_DIRTY.__common: 0x3c8
   - /System/Library/Frameworks/AccessoryLiveActivities.framework/AccessoryLiveActivities
   - /System/Library/Frameworks/AccessoryNotifications.framework/AccessoryNotifications
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
+  - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/CoreImage

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9466
-  Symbols:   8158
-  CStrings:  2194
+  Functions: 9489
+  Symbols:   8172
+  CStrings:  2208
 
Symbols:
+ _CNContactEmailAddressesKey
+ _CNContactPhoneNumbersKey
+ _objc_msgSend$authors
+ _objc_msgSend$contactIdentifier
+ _objc_msgSend$contentCreationDate
+ _objc_msgSend$contentSnippet
+ _objc_msgSend$handleIdentifier
+ _objc_msgSend$handles
+ _objc_msgSend$isCommunicationNotification
+ _objc_msgSend$isGroupThread
+ _objc_msgSend$isTwoFactorCode
+ _objc_msgSend$notificationCritical
+ _objc_msgSend$notificationTimeSensitive
+ _objc_msgSend$primaryRecipients
+ _objc_msgSend$textContent
- _UNCCatchMe
CStrings:
+ "%{public}s Error while indexing without inference %@"
+ "%{public}s Indexing without inference, reason=%s"
+ "%{public}s Not publishing delivery event; notification was not indexed to Spotlight"
+ "CSPerson handles array is empty. %@"
+ "EntityQuery from Spotlight returned %ld results, mapped into %ld entities."
+ "EntityQuery using Spotlight for %{public}ld identifiers"
+ "Failed to query Spotlight fallback: %@"
+ "Falling back to Spotlight for %{public}ld identifiers not hydrated from the repository"
+ "Indexing: %{public}s suppressInference=%{bool,public}d"
+ "UniqueIdentifier workaround is only valid for notification queries."
+ "_kMDItemAppEntityInstanceIdentifier"
+ "indexedNoWaitCMAS"
+ "indexedNoWaitCritical"
+ "indexedNoWaitIgnoreDoNotDisturb"
+ "indexedNoWaitPlatformEligibility"
- "Indexing: %{public}s"
```

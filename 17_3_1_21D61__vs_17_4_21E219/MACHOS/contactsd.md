## contactsd

> `/System/Library/Frameworks/Contacts.framework/Support/contactsd`

```diff

-3631.0.0.0.0
-  __TEXT.__text: 0xcc2c
-  __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_stubs: 0x22c0
-  __TEXT.__objc_methlist: 0xa38
+3632.6.0.0.0
+  __TEXT.__text: 0xd534
+  __TEXT.__auth_stubs: 0x650
+  __TEXT.__objc_stubs: 0x2300
+  __TEXT.__objc_methlist: 0xb54
   __TEXT.__const: 0x117
-  __TEXT.__gcc_except_tab: 0xe4
-  __TEXT.__objc_methname: 0x2d2e
-  __TEXT.__cstring: 0xb5e
-  __TEXT.__objc_classname: 0x1fb
-  __TEXT.__objc_methtype: 0xbf1
+  __TEXT.__gcc_except_tab: 0x108
+  __TEXT.__objc_methname: 0x2d8a
+  __TEXT.__cstring: 0xbd3
+  __TEXT.__objc_classname: 0x24e
+  __TEXT.__objc_methtype: 0xc01
   __TEXT.__dlopen_cstrs: 0xb4
-  __TEXT.__oslogstring: 0x6eb
-  __TEXT.__unwind_info: 0x434
-  __DATA_CONST.__auth_got: 0x330
-  __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__const: 0x960
+  __TEXT.__oslogstring: 0x6d7
+  __TEXT.__unwind_info: 0x47c
+  __DATA_CONST.__auth_got: 0x338
+  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__const: 0x9e8
   __DATA_CONST.__cfstring: 0x500
-  __DATA_CONST.__objc_classlist: 0x70
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x38
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x200
+  __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x1b10
-  __DATA.__objc_selrefs: 0xac8
-  __DATA.__objc_classrefs: 0x1f0
-  __DATA.__objc_superrefs: 0x48
-  __DATA.__objc_ivar: 0x88
-  __DATA.__objc_data: 0x460
-  __DATA.__data: 0x2a0
-  __DATA.__bss: 0x120
+  __DATA.__objc_const: 0x1f30
+  __DATA.__objc_selrefs: 0xad8
+  __DATA.__objc_ivar: 0xb4
+  __DATA.__objc_data: 0x500
+  __DATA.__data: 0x300
+  __DATA.__bss: 0x130
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CF17F54A-E9DB-3035-A022-4A190246A91D
-  Functions: 361
-  Symbols:   188
-  CStrings:  719
+  UUID: 9ABC8779-D688-3C20-A058-7E16397BFC3D
+  Functions: 387
+  Symbols:   191
+  CStrings:  730
 
Symbols:
+ _CNContactProviderSynchronizationReasonScheduledEvent
+ _CNContactsSupportServiceName
+ _CNDataMapperContactProviderServiceName
+ _OBJC_CLASS_$_CNContactProviderManager
+ _OBJC_CLASS_$_CNContactProviderModerator
+ _OBJC_CLASS_$_CNContactProviderSession
+ _OBJC_CLASS_$_CNXPCContactsSupport
+ _OBJC_CLASS_$_CNiOSContactProviderDataMapper
+ _objc_retain_x25
- _CNContactsProviderSynchronizationReasonScheduledEvent
- _CNDataMapperContactsProviderServiceName
- _OBJC_CLASS_$_CNContactsProviderDataMapper
- _OBJC_CLASS_$_CNContactsProviderManager
- _OBJC_CLASS_$_CNContactsProviderModerator
- _OBJC_CLASS_$_CNContactsProviderSession
CStrings:
+ "\x17"
+ "%@ has failed to synchronize all Contact Provider extensions: %@"
+ "%@ has finished synchronizing all Contact Provider extensions."
+ "%@ is running to synchronize all Contact Provider extensions."
+ "@\"CNContactProviderManager\""
+ "@\"ContactsSupportService\"24@?0@\"<CNScheduler>\"8@\"NSXPCConnection\"16"
+ "@40@0:8@16@24@32"
+ "CNXPCContactsSupportService"
+ "ContactsSupportService"
+ "ContactsSupportServiceDelegate"
+ "SynchronizeContactProvidersService"
+ "T@\"CNContactProviderManager\",R,N,V_contactProviderManager"
+ "T@\"NSString\",?,R,C"
+ "_contactProviderManager"
+ "bundleIdentifierForConnection:"
+ "com.apple.contactsd.SynchronizeContactProvidersService"
+ "contactProviderManager"
+ "contacts-connections"
+ "initForContactProvider"
+ "initWithWorkQueue:connection:accessAuthorization:"
+ "isConnectionForContactProvider:"
+ "setContactProviderManager:"
+ "shouldAcceptNewConnection: Accepted [%{public}@, %{public}@]"
+ "shouldAcceptNewConnection: Failed check for TCC uncoupled process %@"
+ "shouldAcceptNewConnection: Not authorized [%{public}@, %{public}@]"
+ "support-connections"
+ "synchronize-contact-providers-service"
+ "synchronizeAllContactProviderExtensions:"
+ "synchronizeContactProviders"
+ "v24@?0@\"NSString\"8@16"
- "%@ has failed to synchronize all Contacts Provider extensions: %@"
- "%@ has finished synchronizing all Contacts Provider extensions."
- "%@ is running to synchronize all Contacts Provider extensions."
- "@\"CNContactsProviderManager\""
- "Couldn't check if contactsd client is a TCC uncoupled process: %@"
- "SynchronizeContactsProvidersService"
- "T@\"CNContactsProviderManager\",R,N,V_contactsProviderManager"
- "_contactsProviderManager"
- "com.apple.contactsd.SynchronizeContactsProvidersService"
- "connections"
- "contactsProviderManager"
- "initForContactsProvider"
- "isClientAuthorizedAccessForConnection: audit token bundle identifier = %@"
- "isConnectionForContactsProvider:"
- "setContactsProviderManager:"
- "shouldAcceptNewConnection: client not authorized, invalidating connection"
- "synchronize-contacts-providers-service"
- "synchronizeAllContactsProviderExtensions:"
- "synchronizeContactsProviders"

```

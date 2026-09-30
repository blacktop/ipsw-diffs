## ClassroomKit

> `/System/Library/PrivateFrameworks/ClassroomKit.framework/ClassroomKit`

```diff

-121.0.0.0.0
-  __TEXT.__text: 0xb1380
+121.62.5.0.0
+  __TEXT.__text: 0xb0bd0
   __TEXT.__auth_stubs: 0xea0
-  __TEXT.__objc_methlist: 0x128a4
+  __TEXT.__objc_methlist: 0x12704
   __TEXT.__const: 0x180
-  __TEXT.__cstring: 0x8644
-  __TEXT.__oslogstring: 0x41d9
+  __TEXT.__cstring: 0x8674
+  __TEXT.__oslogstring: 0x42cb
   __TEXT.__gcc_except_tab: 0x734
   __TEXT.__ustring: 0x37e
-  __TEXT.__unwind_info: 0x3900
-  __TEXT.__objc_classname: 0x435d
-  __TEXT.__objc_methname: 0x22f54
+  __TEXT.__unwind_info: 0x38c8
+  __TEXT.__objc_classname: 0x42a6
+  __TEXT.__objc_methname: 0x22f05
   __TEXT.__objc_methtype: 0x5bf8
-  __TEXT.__objc_stubs: 0x15be0
+  __TEXT.__objc_stubs: 0x15b60
   __DATA_CONST.__got: 0x12a0
   __DATA_CONST.__const: 0x2930
-  __DATA_CONST.__objc_classlist: 0xed8
+  __DATA_CONST.__objc_classlist: 0xeb8
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x440
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6de8
+  __DATA_CONST.__objc_selrefs: 0x6da8
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0xbc8
+  __DATA_CONST.__objc_superrefs: 0xba8
   __DATA_CONST.__objc_arraydata: 0x288
   __AUTH_CONST.__auth_got: 0x760
   __AUTH_CONST.__const: 0x1820
-  __AUTH_CONST.__cfstring: 0x8c20
-  __AUTH_CONST.__objc_const: 0x26230
+  __AUTH_CONST.__cfstring: 0x8b80
+  __AUTH_CONST.__objc_const: 0x25ef0
   __AUTH_CONST.__objc_dictobj: 0x370
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x6e50
-  __DATA.__objc_ivar: 0x1218
+  __AUTH.__objc_data: 0x6d10
+  __DATA.__objc_ivar: 0x1208
   __DATA.__data: 0x3308
   __DATA.__bss: 0x190
   __DATA_DIRTY.__objc_data: 0x2620

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D1A817DD-2ECA-37C0-8ED3-94C16D2A26FB
-  Functions: 6212
-  Symbols:   22248
-  CStrings:  9404
+  UUID: 84222C97-47F5-353C-BEFD-29BE8EC403D4
+  Functions: 6186
+  Symbols:   22156
+  CStrings:  9384
 
Symbols:
+ -[CRKClassroomLockScreenMonitor_iOS classroomLockScreenWantsToDismiss]
+ -[CRKClassroomLockScreenMonitor_iOS isClassroomLockScreenActivated]
+ -[CRKClassroomLockScreenMonitor_iOS setClassroomLockScreenActivated:]
+ -[CRKClassroomLockScreenMonitor_iOS setClassroomLockScreenWantsToDismiss:]
+ _OBJC_IVAR_$_CRKClassroomLockScreenMonitor_iOS._classroomLockScreenActivated
+ _OBJC_IVAR_$_CRKClassroomLockScreenMonitor_iOS._classroomLockScreenWantsToDismiss
+ _OBJC_IVAR_$_CRKClassroomLockScreenMonitor_iOS.mDidActivateObserver
+ _OBJC_IVAR_$_CRKClassroomLockScreenMonitor_iOS.mDidDeactivateObserver
+ _OBJC_IVAR_$_CRKClassroomLockScreenMonitor_iOS.mDidDisappearObserver
+ _OBJC_IVAR_$_CRKClassroomLockScreenMonitor_iOS.mWantsToDismissObserver
+ ___51-[CRKClassroomLockScreenMonitor_iOS startObserving]_block_invoke_3
+ ___51-[CRKClassroomLockScreenMonitor_iOS startObserving]_block_invoke_4
+ ___51-[CRKClassroomLockScreenMonitor_iOS startObserving]_block_invoke_5
+ _objc_msgSend$setClassroomLockScreenActivated:
+ _objc_msgSend$setClassroomLockScreenWantsToDismiss:
- +[CRKIdentityServiceMockingRequest supportsSecureCoding]
- +[CRKIdentitySharingRequestCertificateRequest supportsSecureCoding]
- +[CRKIdentitySharingSendAdvertisingIdentifierAndCertificateRequest supportsSecureCoding]
- +[CRKIdentitySharingSendCertificateRequest supportsSecureCoding]
- -[CRKIdentityServiceMockingRequest encodeWithCoder:]
- -[CRKIdentityServiceMockingRequest initWithCoder:]
- -[CRKIdentityServiceMockingRequest setShouldDisable:]
- -[CRKIdentityServiceMockingRequest shouldDisable]
- -[CRKIdentitySharingRequestCertificateRequest .cxx_destruct]
- -[CRKIdentitySharingRequestCertificateRequest encodeWithCoder:]
- -[CRKIdentitySharingRequestCertificateRequest initWithCoder:]
- -[CRKIdentitySharingRequestCertificateRequest recipient]
- -[CRKIdentitySharingRequestCertificateRequest setRecipient:]
- -[CRKIdentitySharingSendAdvertisingIdentifierAndCertificateRequest .cxx_destruct]
- -[CRKIdentitySharingSendAdvertisingIdentifierAndCertificateRequest activeCertificateData]
- -[CRKIdentitySharingSendAdvertisingIdentifierAndCertificateRequest advertisingIdentifier]
- -[CRKIdentitySharingSendAdvertisingIdentifierAndCertificateRequest encodeWithCoder:]
- -[CRKIdentitySharingSendAdvertisingIdentifierAndCertificateRequest initWithCoder:]
- -[CRKIdentitySharingSendAdvertisingIdentifierAndCertificateRequest recipients]
- -[CRKIdentitySharingSendAdvertisingIdentifierAndCertificateRequest setActiveCertificateData:]
- -[CRKIdentitySharingSendAdvertisingIdentifierAndCertificateRequest setAdvertisingIdentifier:]
- -[CRKIdentitySharingSendAdvertisingIdentifierAndCertificateRequest setRecipients:]
- -[CRKIdentitySharingSendAdvertisingIdentifierAndCertificateRequest setStagedCertificateData:]
- -[CRKIdentitySharingSendAdvertisingIdentifierAndCertificateRequest stagedCertificateData]
- -[CRKIdentitySharingSendCertificateRequest .cxx_destruct]
- -[CRKIdentitySharingSendCertificateRequest activeCertificateData]
- -[CRKIdentitySharingSendCertificateRequest encodeWithCoder:]
- -[CRKIdentitySharingSendCertificateRequest initWithCoder:]
- -[CRKIdentitySharingSendCertificateRequest recipients]
- -[CRKIdentitySharingSendCertificateRequest setActiveCertificateData:]
- -[CRKIdentitySharingSendCertificateRequest setRecipients:]
- -[CRKIdentitySharingSendCertificateRequest setStagedCertificateData:]
- -[CRKIdentitySharingSendCertificateRequest stagedCertificateData]
- _OBJC_CLASS_$_CRKIdentityServiceMockingRequest
- _OBJC_CLASS_$_CRKIdentitySharingRequestCertificateRequest
- _OBJC_CLASS_$_CRKIdentitySharingSendAdvertisingIdentifierAndCertificateRequest
- _OBJC_CLASS_$_CRKIdentitySharingSendCertificateRequest
- _OBJC_IVAR_$_CRKClassroomLockScreenMonitor_iOS.mDidDismissObserver
- _OBJC_IVAR_$_CRKIdentityServiceMockingRequest._shouldDisable
- _OBJC_IVAR_$_CRKIdentitySharingRequestCertificateRequest._recipient
- _OBJC_IVAR_$_CRKIdentitySharingSendAdvertisingIdentifierAndCertificateRequest._activeCertificateData
- _OBJC_IVAR_$_CRKIdentitySharingSendAdvertisingIdentifierAndCertificateRequest._advertisingIdentifier
- _OBJC_IVAR_$_CRKIdentitySharingSendAdvertisingIdentifierAndCertificateRequest._recipients
- _OBJC_IVAR_$_CRKIdentitySharingSendAdvertisingIdentifierAndCertificateRequest._stagedCertificateData
- _OBJC_IVAR_$_CRKIdentitySharingSendCertificateRequest._activeCertificateData
- _OBJC_IVAR_$_CRKIdentitySharingSendCertificateRequest._recipients
- _OBJC_IVAR_$_CRKIdentitySharingSendCertificateRequest._stagedCertificateData
- _OBJC_METACLASS_$_CRKIdentityServiceMockingRequest
- _OBJC_METACLASS_$_CRKIdentitySharingRequestCertificateRequest
- _OBJC_METACLASS_$_CRKIdentitySharingSendAdvertisingIdentifierAndCertificateRequest
- _OBJC_METACLASS_$_CRKIdentitySharingSendCertificateRequest
- __OBJC_$_CLASS_METHODS_CRKIdentityServiceMockingRequest
- __OBJC_$_CLASS_METHODS_CRKIdentitySharingRequestCertificateRequest
- __OBJC_$_CLASS_METHODS_CRKIdentitySharingSendAdvertisingIdentifierAndCertificateRequest
- __OBJC_$_CLASS_METHODS_CRKIdentitySharingSendCertificateRequest
- __OBJC_$_INSTANCE_METHODS_CRKIdentityServiceMockingRequest
- __OBJC_$_INSTANCE_METHODS_CRKIdentitySharingRequestCertificateRequest
- __OBJC_$_INSTANCE_METHODS_CRKIdentitySharingSendAdvertisingIdentifierAndCertificateRequest
- __OBJC_$_INSTANCE_METHODS_CRKIdentitySharingSendCertificateRequest
- __OBJC_$_INSTANCE_VARIABLES_CRKIdentityServiceMockingRequest
- __OBJC_$_INSTANCE_VARIABLES_CRKIdentitySharingRequestCertificateRequest
- __OBJC_$_INSTANCE_VARIABLES_CRKIdentitySharingSendAdvertisingIdentifierAndCertificateRequest
- __OBJC_$_INSTANCE_VARIABLES_CRKIdentitySharingSendCertificateRequest
- __OBJC_$_PROP_LIST_CRKIdentityServiceMockingRequest
- __OBJC_$_PROP_LIST_CRKIdentitySharingRequestCertificateRequest
- __OBJC_$_PROP_LIST_CRKIdentitySharingSendAdvertisingIdentifierAndCertificateRequest
- __OBJC_$_PROP_LIST_CRKIdentitySharingSendCertificateRequest
- __OBJC_CLASS_RO_$_CRKIdentityServiceMockingRequest
- __OBJC_CLASS_RO_$_CRKIdentitySharingRequestCertificateRequest
- __OBJC_CLASS_RO_$_CRKIdentitySharingSendAdvertisingIdentifierAndCertificateRequest
- __OBJC_CLASS_RO_$_CRKIdentitySharingSendCertificateRequest
- __OBJC_METACLASS_RO_$_CRKIdentityServiceMockingRequest
- __OBJC_METACLASS_RO_$_CRKIdentitySharingRequestCertificateRequest
- __OBJC_METACLASS_RO_$_CRKIdentitySharingSendAdvertisingIdentifierAndCertificateRequest
- __OBJC_METACLASS_RO_$_CRKIdentitySharingSendCertificateRequest
- _objc_msgSend$activeCertificateData
- _objc_msgSend$advertisingIdentifier
- _objc_msgSend$recipient
- _objc_msgSend$recipients
- _objc_msgSend$shouldDisable
- _objc_msgSend$stagedCertificateData
CStrings:
+ "Beacon advertiser is calling -registerService because the WPState is on and it wasn't advertising already"
+ "Beacon advertiser is setting isAdvertising to NO because the WPState is off"
+ "Beacon advertiser updated state %{public}@. isAdvertising: %{public}@. beaconAdvertisement: %{public}@"
+ "TB,N,GisClassroomLockScreenActivated,V_classroomLockScreenActivated"
+ "TB,N,V_classroomLockScreenWantsToDismiss"
+ "TB,R,N,GisClassroomLockScreenActivated"
+ "_classroomLockScreenActivated"
+ "_classroomLockScreenWantsToDismiss"
+ "classroomLockScreenActivated"
+ "classroomLockScreenWantsToDismiss"
+ "cls"
+ "com.apple.studentd.lockScreenPluginDidDeactivate"
+ "com.apple.studentd.lockScreenPluginDidDisappear"
+ "com.apple.studentd.lockScreenPluginWillActivate"
+ "isClassroomLockScreenActivated"
+ "mDidActivateObserver"
+ "mDidDeactivateObserver"
+ "mDidDisappearObserver"
+ "mWantsToDismissObserver"
+ "setClassroomLockScreenActivated:"
+ "setClassroomLockScreenWantsToDismiss:"
- "Beacon advertiser updated state %{public}@"
- "CRKIdentityServiceMockingRequest"
- "CRKIdentitySharingRequestCertificateRequest"
- "CRKIdentitySharingSendAdvertisingIdentifierAndCertificateRequest"
- "CRKIdentitySharingSendCertificateRequest"
- "T@\"NSData\",&,N,V_activeCertificateData"
- "T@\"NSData\",&,N,V_stagedCertificateData"
- "T@\"NSSet\",&,N,V_recipients"
- "T@\"NSString\",&,N,V_recipient"
- "T@\"NSUUID\",&,N,V_advertisingIdentifier"
- "TB,N,V_shouldDisable"
- "_activeCertificateData"
- "_advertisingIdentifier"
- "_recipient"
- "_recipients"
- "_shouldDisable"
- "_stagedCertificateData"
- "activeCertificateData"
- "advertisingIdentifier"
- "mDidDismissObserver"
- "recipient"
- "recipients"
- "setActiveCertificateData:"
- "setAdvertisingIdentifier:"
- "setRecipient:"
- "setRecipients:"
- "setShouldDisable:"
- "setStagedCertificateData:"
- "shouldDisable"
- "stagedCertificateData"

```

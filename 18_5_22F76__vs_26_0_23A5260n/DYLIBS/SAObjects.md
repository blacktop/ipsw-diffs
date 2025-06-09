## SAObjects

> `/System/Library/PrivateFrameworks/SAObjects.framework/SAObjects`

```diff

-3405.4.1.0.0
-  __TEXT.__text: 0x3e768
+3500.32.1.0.0
+  __TEXT.__text: 0x3e8fc
   __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__objc_methlist: 0x31ea8
+  __TEXT.__objc_methlist: 0x32050
   __TEXT.__const: 0x9c8
-  __TEXT.__cstring: 0x16135
+  __TEXT.__cstring: 0x1628d
   __TEXT.__unwind_info: 0x39a0
-  __TEXT.__objc_classname: 0x8b6f
-  __TEXT.__objc_methname: 0x29e96
+  __TEXT.__objc_classname: 0x8bb9
+  __TEXT.__objc_methname: 0x2a0a6
   __TEXT.__objc_methtype: 0x49d
   __TEXT.__objc_stubs: 0xf00
   __DATA_CONST.__got: 0x8a0
-  __DATA_CONST.__const: 0xf938
-  __DATA_CONST.__objc_classlist: 0x2dc8
+  __DATA_CONST.__const: 0xf9e0
+  __DATA_CONST.__objc_classlist: 0x2de0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf130
+  __DATA_CONST.__objc_selrefs: 0xf1c0
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__auth_got: 0x1e0
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x2dec0
-  __AUTH_CONST.__objc_const: 0x58b30
+  __AUTH_CONST.__cfstring: 0x2e0e0
+  __AUTH_CONST.__objc_const: 0x58ea8
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x15f40
+  __AUTH.__objc_data: 0x160d0
   __DATA.__objc_ivar: 0x18
   __DATA.__data: 0xfc0
-  __DATA_DIRTY.__objc_data: 0x6a90
+  __DATA_DIRTY.__objc_data: 0x69f0
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BE83F775-A4AB-30B8-AD7A-80271EA54CBD
-  Functions: 14887
-  Symbols:   49426
-  CStrings:  21319
+  UUID: A00F2C77-9DFE-3486-88B7-4105A37BF6D0
+  Functions: 14920
+  Symbols:   49535
+  CStrings:  21377
 
Symbols:
+ -[SAHomeMemberInfo ephemeralUserId]
+ -[SAHomeMemberInfo setEphemeralUserId:]
+ -[SAIntentGroupRunSiriKitExecutor setUserSessionState:]
+ -[SAIntentGroupRunSiriKitExecutor userSessionState]
+ -[SAIntentGroupRunSiriKitExecutorCompleted setTopicSwitchDetected:]
+ -[SAIntentGroupRunSiriKitExecutorCompleted topicSwitchDetected]
+ -[SARDRunPOMMESRequest selectedUserAttributes]
+ -[SARDRunPOMMESRequest setSelectedUserAttributes:]
+ -[SASelectedUserAttributes encodedClassName]
+ -[SASelectedUserAttributes groupIdentifier]
+ -[SASelectedUserAttributes lowScoreThreshold]
+ -[SASelectedUserAttributes meetsPersonalRequestThreshold]
+ -[SASelectedUserAttributes meetsUserSessionThreshold]
+ -[SASelectedUserAttributes score]
+ -[SASelectedUserAttributes setLowScoreThreshold:]
+ -[SASelectedUserAttributes setMeetsPersonalRequestThreshold:]
+ -[SASelectedUserAttributes setMeetsUserSessionThreshold:]
+ -[SASelectedUserAttributes setScore:]
+ -[SASelectedUserAttributes setUserIdentityClassification:]
+ -[SASelectedUserAttributes userIdentityClassification]
+ -[SAUIContinueAppIntentOnDevice appIntentData]
+ -[SAUIContinueAppIntentOnDevice encodedClassName]
+ -[SAUIContinueAppIntentOnDevice groupIdentifier]
+ -[SAUIContinueAppIntentOnDevice requiresResponse]
+ -[SAUIContinueAppIntentOnDevice setAppIntentData:]
+ -[SAUserSessionState encodedClassName]
+ -[SAUserSessionState groupIdentifier]
+ -[SAUserSessionState isHighConfidenceSession]
+ -[SAUserSessionState isSessionActiveForRecognizedUser]
+ -[SAUserSessionState setIsHighConfidenceSession:]
+ -[SAUserSessionState setIsSessionActiveForRecognizedUser:]
+ -[SAUserSessionState setUserSessionType:]
+ -[SAUserSessionState userSessionType]
+ _OBJC_CLASS_$_SASelectedUserAttributes
+ _OBJC_CLASS_$_SAUIContinueAppIntentOnDevice
+ _OBJC_CLASS_$_SAUserSessionState
+ _OBJC_METACLASS_$_SASelectedUserAttributes
+ _OBJC_METACLASS_$_SAUIContinueAppIntentOnDevice
+ _OBJC_METACLASS_$_SAUserSessionState
+ _SADeviceRestrictionCAR_OWNS_MAIN_AUDIOValue
+ _SAHomeMemberInfoEphemeralUserIdPListKey
+ _SAIntentGroupRunSiriKitExecutorCompletedTopicSwitchDetectedPListKey
+ _SAIntentGroupRunSiriKitExecutorUserSessionStatePListKey
+ _SARDRunPOMMESRequestSelectedUserAttributesPListKey
+ _SASelectedUserAttributesClassIdentifier
+ _SASelectedUserAttributesLowScoreThresholdPListKey
+ _SASelectedUserAttributesMeetsPersonalRequestThresholdPListKey
+ _SASelectedUserAttributesMeetsUserSessionThresholdPListKey
+ _SASelectedUserAttributesScorePListKey
+ _SASelectedUserAttributesUserIdentityClassificationPListKey
+ _SAUIContinueAppIntentOnDeviceAppIntentDataPListKey
+ _SAUIContinueAppIntentOnDeviceClassIdentifier
+ _SAUserInterfaceIdiomMARGARITAValue
+ _SAUserSessionStateClassIdentifier
+ _SAUserSessionStateIsHighConfidenceSessionPListKey
+ _SAUserSessionStateIsSessionActiveForRecognizedUserPListKey
+ _SAUserSessionStateUserSessionTypePListKey
+ _SAUserSessionTypeAmbientValue
+ _SAUserSessionTypeEnrolledUserSessionValue
+ _SAUserSessionTypeGuestUserSessionValue
+ __OBJC_$_CLASS_PROP_LIST_SASelectedUserAttributes
+ __OBJC_$_CLASS_PROP_LIST_SAUserSessionState
+ __OBJC_$_INSTANCE_METHODS_SASelectedUserAttributes
+ __OBJC_$_INSTANCE_METHODS_SAUIContinueAppIntentOnDevice
+ __OBJC_$_INSTANCE_METHODS_SAUserSessionState
+ __OBJC_$_PROP_LIST_SASelectedUserAttributes
+ __OBJC_$_PROP_LIST_SAUIContinueAppIntentOnDevice
+ __OBJC_$_PROP_LIST_SAUserSessionState
+ __OBJC_CLASS_PROTOCOLS_$_SASelectedUserAttributes
+ __OBJC_CLASS_PROTOCOLS_$_SAUserSessionState
+ __OBJC_CLASS_RO_$_SASelectedUserAttributes
+ __OBJC_CLASS_RO_$_SAUIContinueAppIntentOnDevice
+ __OBJC_CLASS_RO_$_SAUserSessionState
+ __OBJC_METACLASS_RO_$_SASelectedUserAttributes
+ __OBJC_METACLASS_RO_$_SAUIContinueAppIntentOnDevice
+ __OBJC_METACLASS_RO_$_SAUserSessionState
CStrings:
+ "Ambient"
+ "CAR_OWNS_MAIN_AUDIO"
+ "ContinueAppIntentOnDevice"
+ "EnrolledUserSession"
+ "GuestUserSession"
+ "MARGARITA"
+ "SASelectedUserAttributes"
+ "SAUIContinueAppIntentOnDevice"
+ "SAUserSessionState"
+ "SelectedUserAttributes"
+ "T@\"SASelectedUserAttributes\",&,N"
+ "T@\"SAUIAppIntentData\",&,N"
+ "T@\"SAUserSessionState\",&,N"
+ "UserSessionState"
+ "appIntentData"
+ "isHighConfidenceSession"
+ "isSessionActiveForRecognizedUser"
+ "meetsPersonalRequestThreshold"
+ "meetsUserSessionThreshold"
+ "selectedUserAttributes"
+ "setAppIntentData:"
+ "setIsHighConfidenceSession:"
+ "setIsSessionActiveForRecognizedUser:"
+ "setMeetsPersonalRequestThreshold:"
+ "setMeetsUserSessionThreshold:"
+ "setSelectedUserAttributes:"
+ "setTopicSwitchDetected:"
+ "setUserSessionState:"
+ "setUserSessionType:"
+ "topicSwitchDetected"
+ "userSessionState"
+ "userSessionType"

```

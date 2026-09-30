## callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

-1576.500.201.2.4
-  __TEXT.__text: 0x4c7d1c
-  __TEXT.__auth_stubs: 0x4dd0
-  __TEXT.__objc_stubs: 0x3abc0
-  __TEXT.__objc_methlist: 0x275d0
-  __TEXT.__objc_classname: 0x56e7
-  __TEXT.__objc_methname: 0x6a22f
-  __TEXT.__cstring: 0x1b64d
-  __TEXT.__objc_methtype: 0x1298f
-  __TEXT.__const: 0xec08
-  __TEXT.__oslogstring: 0x4db13
-  __TEXT.__gcc_except_tab: 0x2984
+1576.600.4.0.0
+  __TEXT.__text: 0x4d1218
+  __TEXT.__auth_stubs: 0x4e20
+  __TEXT.__objc_stubs: 0x3aca0
+  __TEXT.__objc_methlist: 0x27600
+  __TEXT.__objc_classname: 0x5717
+  __TEXT.__objc_methname: 0x6a297
+  __TEXT.__cstring: 0x1b67d
+  __TEXT.__objc_methtype: 0x1297f
+  __TEXT.__const: 0xecb8
+  __TEXT.__oslogstring: 0x4e4d3
+  __TEXT.__gcc_except_tab: 0x296c
   __TEXT.__ustring: 0x10
-  __TEXT.__swift5_typeref: 0x8960
+  __TEXT.__swift5_typeref: 0x89e4
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x9294
+  __TEXT.__constg_swiftt: 0x92c8
   __TEXT.__swift5_builtin: 0x6cc
-  __TEXT.__swift5_reflstr: 0x7ed3
-  __TEXT.__swift5_fieldmd: 0x6710
+  __TEXT.__swift5_reflstr: 0x7f93
+  __TEXT.__swift5_fieldmd: 0x6780
   __TEXT.__swift5_assocty: 0x950
-  __TEXT.__swift5_proto: 0x8dc
-  __TEXT.__swift5_types: 0x670
-  __TEXT.__swift5_capture: 0x3834
+  __TEXT.__swift5_proto: 0x8e0
+  __TEXT.__swift5_types: 0x674
+  __TEXT.__swift5_capture: 0x3938
   __TEXT.__swift5_protos: 0x184
   __TEXT.__swift_as_entry: 0x228
   __TEXT.__swift_as_ret: 0x270
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0xe940
-  __TEXT.__eh_frame: 0x9368
-  __DATA_CONST.__auth_got: 0x26f8
-  __DATA_CONST.__got: 0x2488
-  __DATA_CONST.__auth_ptr: 0x13a8
-  __DATA_CONST.__const: 0x18588
+  __TEXT.__unwind_info: 0xe990
+  __TEXT.__eh_frame: 0x92fc
+  __DATA_CONST.__auth_got: 0x2720
+  __DATA_CONST.__got: 0x2498
+  __DATA_CONST.__auth_ptr: 0x13c8
+  __DATA_CONST.__const: 0x187c8
   __DATA_CONST.__cfstring: 0xb040
-  __DATA_CONST.__objc_classlist: 0xc50
+  __DATA_CONST.__objc_classlist: 0xc58
   __DATA_CONST.__objc_catlist: 0x140
   __DATA_CONST.__objc_protolist: 0xad8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x228
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x3caa0
-  __DATA.__objc_selrefs: 0x12918
-  __DATA.__objc_ivar: 0x1e40
-  __DATA.__objc_data: 0xdb20
-  __DATA.__data: 0xfbb8
+  __DATA.__objc_const: 0x3cc48
+  __DATA.__objc_selrefs: 0x12958
+  __DATA.__objc_ivar: 0x1e44
+  __DATA.__objc_data: 0xdc18
+  __DATA.__data: 0xfbf8
   __DATA.__bss: 0xda90
-  __DATA.__common: 0xa30
+  __DATA.__common: 0xa38
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AC83D841-C117-38FC-8318-9ACF43E914B1
-  Functions: 25071
-  Symbols:   2653
-  CStrings:  25151
+  UUID: 17D24378-82B0-3B96-9980-56D220F0C5C3
+  Functions: 25140
+  Symbols:   2661
+  CStrings:  25188
 
Symbols:
+ _$s10Foundation20PersonNameComponentsV19_bridgeToObjectiveCSo08NSPersoncD0CyF
+ _$s10Foundation20PersonNameComponentsVMa
+ _$s10Foundation20PersonNameComponentsVMn
+ _OBJC_CLASS_$_INPerson
+ _OBJC_CLASS_$_INPersonHandle
+ _TUIsInternationalHandle
+ _TUIsInternationalRecentCall
+ _TUMinimumSupportedSharePlayProtocolVersion
CStrings:
+ "%@ is handling providersChangedForProviderManager %@, with service providers %@"
+ "%@ is ignoring providersChangedForProviderManager because keychain is invalid"
+ "%s count: %ld isAmbiguous: %{bool}d"
+ "%s is handling %s"
+ "%s: %s"
+ "%s: >>> shouldHideNotification: FaceTime call, but not unknown, skipping..."
+ "%s: >>> shouldHideNotification: FaceTime call, but notifications are not hidden, skipping..."
+ "%s: >>> shouldHideNotification: not a FaceTime call, skipping..."
+ "%s: Adding call with identifier %s to the callsToPost array"
+ "%s: Adding call with identifier %s to the pendingCallIdentifiers set"
+ "%s: Adding notification request %@ for missed call %s"
+ "%s: Adding notification request %@ to %s"
+ "%s: Adding notification with count: %ld"
+ "%s: Already posted forwarding notification for call %s"
+ "%s: Answering call %s from notification forwarding action"
+ "%s: Asked to post %ld voicemails"
+ "%s: Asked to update %ld voicemail notifications"
+ "%s: Attempt to create a notification attachment for file at %s failed with error %@"
+ "%s: Block emailAddress %s from notification"
+ "%s: Block phoneNumber: %s from notification, formatted phonenumber: %@"
+ "%s: Call interactions changed"
+ "%s: Conversation UUID %s had a state change, and we determined that we should post an invite notification"
+ "%s: Could not create App Store URL for bundleID: %{public}s"
+ "%s: Could not extract call UUID from notification identifier %{public}s"
+ "%s: Could not find active conversation in conversations: %s"
+ "%s: Could not find notification provider for action"
+ "%s: Could not find recent call with identifier: %s"
+ "%s: Could not find required userInfo keys for SharePlay notification: %{public}s"
+ "%s: Could not find voicemail with identifier: %s"
+ "%s: Could not retrieve date of most recent call for notification provider %@"
+ "%s: Could not retrieve date of most recent voicemail for notification provider %@"
+ "%s: Could not update notification content; using original notification content for call with identifier %s"
+ "%s: Could not update notification content; using original notification content for voicemail message with identifier %lu"
+ "%s: Couldn't find call with UUID %{public}s"
+ "%s: Cound not retrieve intent; using original notification content for voicemail message with identifier %lu"
+ "%s: Cound not retrieve interaction; using original notification content for call with identifier %s"
+ "%s: Cound not retrieve start call intent from %@"
+ "%s: Cound not retrieve voicemail message; using original notification content for voicemail message with identifier %lu"
+ "%s: Created and sent a joinRequest for conversation %@"
+ "%s: Creating XPC endpoint for User notifications"
+ "%s: Deallocating %@"
+ "%s: Declining call %s from notification forwarding action"
+ "%s: Delaying invite notification because a paired device is connected"
+ "%s: Delivering user notification for new activity session: %@"
+ "%s: Did not find expected call recording information"
+ "%s: Did not find expected pending chat information"
+ "%s: Did not find expected pending chat uuid information"
+ "%s: Encountered undefined FaceTime media type %s"
+ "%s: Error while posting notification: %@"
+ "%s: Error while replacing notification: %@"
+ "%s: Failed to construct FaceTime app URL to view link details"
+ "%s: Failed to determine conversation link for pending member notification with conversation %s and conversationLink %s"
+ "%s: Failed to donate interaction: %@"
+ "%s: Failed to open URL %s#. Error %@"
+ "%s: Failed to open activity session with identifier: %s error: %{public}@"
+ "%s: Failed to update notification content with intent: %@"
+ "%s: Generating notification for new launch state: %{public}lu activity session: %{public}s"
+ "%s: Generating notification for notice type: %{public}s and notice: %{public}s"
+ "%s: Got voicemail info for uuid %s to available: %{bool}d, count: %@"
+ "%s: Handle momentsStartedRemoteCapture in-app %s"
+ "%s: Handling notification %s"
+ "%s: Handling notification for pending message did receive invite: %s"
+ "%s: Handling voicemailInfoAvailableNotification voicemailInfo: %@, context: %@"
+ "%s: Handoff eligibility changed for %@"
+ "%s: Ignoring adding notification request %@ since valid network is not reachable"
+ "%s: Ignoring notice for foreground application with existing activity session: %s"
+ "%s: Ignoring notification response %s because a handoff dynamic identifier is missing/could not be typecasted in userInfo"
+ "%s: Ignoring notification response %s because a pseudonym is missing/could not be typecasted in userInfo"
+ "%s: In response to conversations changed, we determined that we should post an invite notification for conversation UUID %s"
+ "%s: InCallService changed to non-running state (%s); updating posted notifications"
+ "%s: Invalid groupUUID or conversation not found for notification: %{public}s"
+ "%s: Launched application for activity session %{public}s"
+ "%s: Launching FaceTime for notification response via url %s"
+ "%s: Loaded user notification controller"
+ "%s: Looking to merge badge count data"
+ "%s: Missing activitySessionIdentifier for Show SharePlay notification: %{public}s"
+ "%s: Missing bundleID to perform get the app for notification: %{public}s"
+ "%s: Most recent call date is now %s for notification provider %@"
+ "%s: Most recent voicemail date is now %s for notification provider %@"
+ "%s: No conversation is waiting to post a notification for uuid %s so not posting invite notification"
+ "%s: No current unsubscribed voicemail info, attempting to update..."
+ "%s: No notification for conversation UUID %s"
+ "%s: Not posting LMI approval notification because the conversation is currently showing on screen"
+ "%s: Not posting handoff nearby notification for conversation %s because it did not have handoff eligibility"
+ "%s: Not posting notification as detected locally ended screen sharing for notice: %{public}s with participant: %{public}@"
+ "%s: Not posting notification for activity because conversation is not joined or telephonyProvider"
+ "%s: Not posting notification for activity session start notice: %@ on conversation: %@ since activitySessionLaunch has already posted"
+ "%s: Not posting notification for activity session start notice: %@ on conversation: %@ since activitySessionLaunch has not already posted"
+ "%s: Not posting notification for launched activity session because it's locally originated"
+ "%s: Not posting notification for translation activity"
+ "%s: Not posting notification for translation activity session"
+ "%s: Not posting notification for unsupported foreground application: %{public}s, %{public}s"
+ "%s: Not posting notification for unsupported notice: %{public}@"
+ "%s: Not posting notification since it is restricted by the call filter"
+ "%s: Not posting pending member notification becaue Group FaceTime is not supported (GreenTea device or doesn't support multiway)"
+ "%s: Not posting user notification for handoff eligible conversation %s because there's already a local non-waiting conversation"
+ "%s: Notification provider %@ found missed calls %s"
+ "%s: Online status changed: %s"
+ "%s: Opening App Store for bundleID: %{public}s"
+ "%s: Performed dial request: %@"
+ "%s: Performed join conversation request: %@"
+ "%s: Performing dial request: %@ ended in error: %@"
+ "%s: Posting forwarding notification for call %s"
+ "%s: Posting notification for activity session launch: %@ on conversation: %@"
+ "%s: Posting notification for activity session notice: %@ on conversation: %@"
+ "%s: Posting notification request %@ for handoff eligible conversation UUID %s nearby"
+ "%s: Posting notification request for conversation UUID %s with content %@"
+ "%s: Received %ld new voicemails since date %s"
+ "%s: Received %ld new voicemails since date %s: %s"
+ "%s: Received invalid notification object for foreground application change notification: %s"
+ "%s: Received response with identifier %{public}s"
+ "%s: Recent call was a silenced unknown caller; displaying notification as an alert (%@)"
+ "%s: Removing all voicemail notifications. Current notification identifiers: %s"
+ "%s: Removing forwarding notification for call %s"
+ "%s: Removing handoff eligible nearby notification for conversation UUID %s"
+ "%s: Removing handoff notification as there are no handoff-eligible conversations left"
+ "%s: Removing invite notification for conversation UUID %s with notification identifier %s"
+ "%s: Removing notification with identifier %s from %s"
+ "%s: Removing pending notification for conversation with uuid %s since we are joined into the conversation"
+ "%s: Removing posted voicemail notifications because vmd isn't subscribed."
+ "%s: Replacing handoff eligible nearby notification from old conversation UUID %s to new conversation UUID %s"
+ "%s: Replacing notification id %s with content %@"
+ "%s: Replacing notification with identifier %s from %s"
+ "%s: Retrieved intent; updating notification content for voicemail message with identifier %lu"
+ "%s: Retrieved interaction; retrieving intent for call with identifier %s"
+ "%s: Retrieved start call intent; updating notification content for call with identifier %s"
+ "%s: Retrieving inbox voicemail messages failed with error %@"
+ "%s: Retrieving messages delivered after %s"
+ "%s: Retrieving voicemail messages failed with error %@"
+ "%s: SharePlay force disabled, not posting foreground application notification."
+ "%s: SharePlay force disabled, not posting new activity session notification."
+ "%s: SharePlay force disabled, not posting notification for notice."
+ "%s: Showing \"Get the App\" because app for the activity is not installed"
+ "%s: Showing \"Join SharePlay\" because activity is supported"
+ "%s: Showing \"Open in Safari\" because activity is supported in web browser"
+ "%s: Skip posting pending member notification because hasJoined: %{bool}d, ignoreLMIRequests: %{bool}d for conversation: %@"
+ "%s: Skipping notification for FaceTime call with identifier %s"
+ "%s: Skipping update of call history notification; InCallService process state is foreground running. %@"
+ "%s: Started broadcasting User notifications mach service with %@"
+ "%s: Subscription status changed: %s"
+ "%s: Successfully posted notification with identifier: %s"
+ "%s: Successfully replaced notification with identifier: %s"
+ "%s: Time since LMI initiated for member %@ is %s seconds"
+ "%s: Tracked pending member changed, but not a locally owned link -- ignoring %@ %@"
+ "%s: UNUserNotificationCenter received response %@"
+ "%s: Unable to block handles because handles are nil"
+ "%s: Unable to block the emailAddress handle %s because handle.normalizedValue = nil"
+ "%s: Unable to block the phoneNumber handle %s because handle.normalizedValue = nil"
+ "%s: Unhandled action identifier '%{public}s' for call %s"
+ "%s: Unknown notification response received"
+ "%s: Unknown notification response received %{public}s"
+ "%s: Updated providers"
+ "%s: Updating call history badge count for notification provider %@"
+ "%s: Updating conversation for pending invite notification"
+ "%s: Updating providers"
+ "%s: Updating voicemail info for uuid %s to available: %{bool}d, count: %ld"
+ "%s: User requested to view application for activity session: %{public}s"
+ "%s: Voicemail is not MWI - Ignoring voicemailInfoAvailableNotification"
+ "%s: Voicemail is not subscribed"
+ "%s: Voicemail store changed, and we found the following voicemail messages we were waiting for: %s"
+ "%s: Voicemail store changed, but we did not find any voicemail messages we were waiting for. Waiting for: %s"
+ "%s: Voicemail store changed. We were waiting for %s and found %s"
+ "%s: Voicemails changed: %s"
+ "%s: We have %ld calls to post (pendingCallIdentifiers: %s)"
+ "%s: We have a voicemail provider, so setting isAmbiguous"
+ "%s: [WARN] Could not generate dial request URL for voicemail: %s"
+ "%s: continueActivity action for notification: %s"
+ "%s: continueActivity action for notification: %{public}s"
+ "%s: could not find conversation for notification stream token: %s"
+ "%s: could not find conversation or call for notification stream token: %s"
+ "%s: could not find participant for participant in conversation: %@ for requesterID: %s"
+ "%s: does not handle response with identifier %s"
+ "%s: momentsStartedRemoteCapture received invalid notification object: %s"
+ "%s: requestScreenShare action for notification: %{public}s"
+ "%s: unknown handle type: %s"
+ "At least one participant in conversation %@ does not support SharePlay. Invalidating session %@"
+ "Could not find value from keychain %@: %@"
+ "Could not save value to keychain %@: %@"
+ "Deleted %ld recent calls for removed providers"
+ "H"
+ "INCOMING_CALL_FORWARDING_ACCEPT"
+ "INCOMING_CALL_FORWARDING_DECLINE"
+ "Low power mode is enabled, not extracting name or summary"
+ "Not adding activity session, as not all participants are on the latest SharePlay version"
+ "Not enforcing shareplay version check due to server over-ride"
+ "Recording is not allowed when in Lockdown Mode"
+ "Should we send to AnsweringMachine? shouldSendToLVM=%@ shouldSendToReceptionist=%@ noOtherCalls=%@ homeCountry=%@ hasSpamIdentifierInCarrierName=%@ isAnsweringMachineAvailable=%@ isAutoAnswerDevice=%@ isLowPowerModeEnabled=%@"
+ "[WARN] All active participants in the call are not on minimum supported shareplay version"
+ "[WARN] One or more participant on %@ is on an older share play protocol %@ version %@"
+ "[WARN] Setting should ignore session to YES because the system is preventing the incoming call for destinationID %@ and provider %@"
+ "_TtC13callservicesd42IncomingCallNotificationForwardingProvider"
+ "callerID from service %@: %@"
+ "callerID from service is invalid, fetching callerID from active local handles: %@"
+ "callservicesd.IncomingCallNotificationForwardingProvider"
+ "deleteCallsForRemovedProvidersWithKeptProviders:completion:"
+ "faceTimeHideNotifications"
+ "faceTimeNewCallersFilterMode"
+ "ftCallFilteringHideNotificationsEnabled"
+ "incoming-call-forwarding"
+ "incoming-call-forwarding-"
+ "incoming-call-forwarding-accept"
+ "incoming-call-forwarding-decline"
+ "incomingCallNotificationForwardingEnabled"
+ "initWithCallRecordFilter:callRecordToCallBack:audioRoute:destinationType:contacts:callCapability:"
+ "initWithPersonHandle:nameComponents:displayName:image:contactIdentifier:customIdentifier:"
+ "initWithValue:type:"
+ "notificationIdentifiersByCallUUID"
- "%@ count: %ld isAmbiguous: %{bool}d"
- "%@ does not handle response with identifier %@"
- "%@ does not handle response with identifier %s"
- "%@ is handling %s"
- "%@ is handling providersChangedForProviderManager %@, with keychainIsValid: YES and remoteClient: YES"
- "%s"
- "%{public}@: Could not find active conversation in conversations: %s"
- "%{public}@: Ignoring notice for foreground application with existing activity session: %s"
- "%{public}@: Received invalid notification object for foreground application change notification: %s"
- "Adding call with identifier %s to the callsToPost array"
- "Adding call with identifier %s to the pendingCallIdentifiers set"
- "Adding notification request %@ for missed call %s"
- "Adding notification request %@ to %s"
- "Adding notification with count: %ld"
- "Asked to post %ld voicemails"
- "Asked to update %ld voicemail notifications"
- "Attempt to create a notification attachment for file at %s failed with error %@"
- "Block emailAddress %s from notification"
- "Block phoneNumber: %s from notification, formatted phonenumber: %@"
- "Call interactions changed"
- "Conversation UUID %s had a state change, and we determined that we should post an invite notification"
- "Could not create App Store URL for bundleID: %{public}s"
- "Could not find notification provider for action"
- "Could not find recent call with identifier: %s"
- "Could not find required userInfo keys for SharePlay notification: %{public}s"
- "Could not find value from keychain: %@"
- "Could not find voicemail with identifier: %s"
- "Could not retrieve date of most recent call for notification provider %@"
- "Could not retrieve date of most recent voicemail for notification provider %@"
- "Could not update notification content; using original notification content for call with identifier %s"
- "Could not update notification content; using original notification content for voicemail message with identifier %lu"
- "Cound not retrieve intent; using original notification content for voicemail message with identifier %lu"
- "Cound not retrieve interaction; using original notification content for call with identifier %s"
- "Cound not retrieve start call intent from %@"
- "Cound not retrieve voicemail message; using original notification content for voicemail message with identifier %lu"
- "Created and sent a joinRequest for conversation %@"
- "Creating XPC endpoint for User notifications"
- "Deallocating %@"
- "Delaying invite notification because a paired device is connected"
- "Deleted %ld recent calls matching predicate %@"
- "Delivering user notification for new activity session: %@"
- "Did not find expected call recording information"
- "Did not find expected pending chat information"
- "Did not find expected pending chat uuid information"
- "Encountered undefined FaceTime media type %s"
- "Error while posting notification: %@"
- "Error while replacing notification: %@"
- "Failed to construct FaceTime app URL to view link details"
- "Failed to determine conversation link for pending member notification with conversation %s and conversationLink %s"
- "Failed to donate interaction: %@"
- "Failed to open URL %s#. Error %@"
- "Failed to open activity session with identifier: %s error: %{public}@"
- "G"
- "Generating notification for new launch state: %{public}lu activity session: %{public}s"
- "Generating notification for notice type: %{public}s and notice: %{public}s"
- "Got voicemail info for uuid %s to available: %{bool}d, count: %@"
- "Handle momentsStartedRemoteCapture in-app %s"
- "Handling notification %@"
- "Handling notification %s"
- "Handling notification for pending message did receive invite: %s"
- "Handling voicemailInfoAvailableNotification voicemailInfo: %@, context: %@"
- "Handoff eligibility changed for %@"
- "Ignoring adding notification request %@ since valid network is not reachable"
- "Ignoring notification response %s because a handoff dynamic identifier is missing/could not be typecasted in userInfo"
- "Ignoring notification response %s because a pseudonym is missing/could not be typecasted in userInfo"
- "Ignoring providers changed callbck because keychainIsValid was false"
- "In response to conversations changed, we determined that we should post an invite notification for conversation UUID %s"
- "InCallService changed to non-running state (%s); updating posted notifications"
- "Invalid groupUUID or conversation not found for notification: %{public}s"
- "Launched application for activity session %{public}s"
- "Launching FaceTime for notification response via url %s"
- "Loaded user notification controller"
- "Looking to merge badge count data"
- "Missing activitySessionIdentifier for Show SharePlay notification: %{public}s"
- "Missing bundleID to perform get the app for notification: %{public}s"
- "Most recent call date is now %s for notification provider %@"
- "Most recent voicemail date is now %s for notification provider %@"
- "No conversation is waiting to post a notification for uuid %s so not posting invite notification"
- "No current unsubscribed voicemail info, attempting to update..."
- "No notification for conversation UUID %s"
- "Not posting LMI approval notification because the conversation is currently showing on screen"
- "Not posting handoff nearby notification for conversation %s because it did not have handoff eligibility"
- "Not posting notification as detected locally ended screen sharing for notice: %{public}s with participant: %{public}@"
- "Not posting notification for activity because conversation is not joined or telephonyProvider"
- "Not posting notification for activity session start notice: %@ on conversation: %@ since activitySessionLaunch has already posted"
- "Not posting notification for activity session start notice: %@ on conversation: %@ since activitySessionLaunch has not already posted"
- "Not posting notification for launched activity session because it's locally originated"
- "Not posting notification for translation activity"
- "Not posting notification for translation activity session"
- "Not posting notification for unsupported foreground application: %{public}s, %{public}s"
- "Not posting notification for unsupported notice: %{public}@"
- "Not posting notification since it is restricted by the call filter"
- "Not posting pending member notification becaue Group FaceTime is not supported (GreenTea device or doesn't support multiway)"
- "Not posting user notification for handoff eligible conversation %s because there's already a local non-waiting conversation"
- "Notification provider %@ found missed calls %s"
- "Online status changed: %s"
- "Opening App Store for bundleID: %{public}s"
- "Performed dial request: %@"
- "Performed join conversation request: %@"
- "Performing dial request: %@ ended in error: %@"
- "Posting notification for activity session launch: %@ on conversation: %@"
- "Posting notification for activity session notice: %@ on conversation: %@"
- "Posting notification request %@ for handoff eligible conversation UUID %s nearby"
- "Posting notification request for conversation UUID %s with content %@"
- "Received %ld new voicemails since date %s"
- "Received %ld new voicemails since date %s: %s"
- "Received response with identifier %{public}s"
- "Recent call was a silenced unknown caller; displaying notification as an alert (%@)"
- "Removing all voicemail notifications. Current notification identifiers: %s"
- "Removing handoff eligible nearby notification for conversation UUID %s"
- "Removing handoff notification as there are no handoff-eligible conversations left"
- "Removing invite notification for conversation UUID %s with notification identifier %s"
- "Removing notification with identifier %s from %s"
- "Removing pending notification for conversation with uuid %s since we are joined into the conversation"
- "Removing posted voicemail notifications because vmd isn't subscribed."
- "Replacing handoff eligible nearby notification from old conversation UUID %s to new conversation UUID %s"
- "Replacing notification id %s with content %@"
- "Replacing notification with identifier %s from %s"
- "Retrieved intent; updating notification content for voicemail message with identifier %lu"
- "Retrieved interaction; retrieving intent for call with identifier %s"
- "Retrieved start call intent; updating notification content for call with identifier %s"
- "Retrieving inbox voicemail messages failed with error %@"
- "Retrieving messages delivered after %s"
- "Retrieving voicemail messages failed with error %@"
- "SharePlay force disabled, not posting foreground application notification."
- "SharePlay force disabled, not posting new activity session notification."
- "SharePlay force disabled, not posting notification for notice."
- "Should we send to AnsweringMachine? shouldSendToLVM=%@ shouldSendToReceptionist=%@ noOtherCalls=%@ homeCountry=%@ hasSpamIdentifierInCarrierName=%@ isAnsweringMachineAvailable=%@ isAutoAnswerDevice=%@"
- "Showing \"Get the App\" because app for the activity is not installed"
- "Showing \"Join SharePlay\" because activity is supported"
- "Showing \"Open in Safari\" because activity is supported in web browser"
- "Skip posting pending member notification because hasJoined: %{bool}d, ignoreLMIRequests: %{bool}d for conversation: %@"
- "Skipping update of call history notification; InCallService process state is foreground running. %@"
- "Started broadcasting User notifications mach service with %@"
- "Subscription status changed: %s"
- "Successfully posted notification with identifier: %s"
- "Successfully replaced notification with identifier: %s"
- "Time since LMI initiated for member %@ is %s seconds"
- "Tracked pending member changed, but not a locally owned link -- ignoring %@ %@"
- "UNUserNotificationCenter received response %@"
- "Unable to block handles because handles are nil"
- "Unable to block the emailAddress handle %s because handle.normalizedValue = nil"
- "Unable to block the phoneNumber handle %s because handle.normalizedValue = nil"
- "Unknown notification response received"
- "Unknown notification response received %{public}s"
- "Updated providers"
- "Updating call history badge count for notification provider %@"
- "Updating conversation for pending invite notification"
- "Updating providers"
- "Updating voicemail info for uuid %s to available: %{bool}d, count: %ld"
- "User requested to view application for activity session: %{public}s"
- "Voicemail is not MWI - Ignoring voicemailInfoAvailableNotification"
- "Voicemail is not subscribed"
- "Voicemail store changed, and we found the following voicemail messages we were waiting for: %s"
- "Voicemail store changed, but we did not find any voicemail messages we were waiting for. Waiting for: %s"
- "Voicemail store changed. We were waiting for %s and found %s"
- "Voicemails changed: %s"
- "We have %ld calls to post (pendingCallIdentifiers: %s)"
- "We have a voicemail provider, so setting isAmbiguous"
- "[WARN] Could not generate dial request URL for voicemail: %s"
- "continueActivity action for notification: %s"
- "continueActivity action for notification: %{public}s"
- "could not find conversation for notification stream token: %s"
- "could not find conversation or call for notification stream token: %s"
- "could not find participant for participant in conversation: %@ for requesterID: %s"
- "isLocalState"
- "momentsStartedRemoteCapture received invalid notification object: %s"
- "requestScreenShare action for notification: %{public}s"
- "unknown handle type: %s"
- "v24@0:8I16I20"

```

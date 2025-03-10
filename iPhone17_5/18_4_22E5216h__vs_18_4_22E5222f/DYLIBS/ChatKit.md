## ChatKit

> `/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit`

```diff

-1402.500.164.2.1
-  __TEXT.__text: 0x8974ec
-  __TEXT.__auth_stubs: 0x8d10
+1402.500.172.2.1
+  __TEXT.__text: 0x8985cc
+  __TEXT.__auth_stubs: 0x8d00
   __TEXT.__delay_helper: 0x258
   __TEXT.__objc_methlist: 0x6972c
   __TEXT.__const: 0x1dcd4
-  __TEXT.__gcc_except_tab: 0x26c58
-  __TEXT.__cstring: 0x41b79
-  __TEXT.__oslogstring: 0x3ef5b
+  __TEXT.__gcc_except_tab: 0x26dc0
+  __TEXT.__cstring: 0x41fb9
+  __TEXT.__oslogstring: 0x3f5cb
   __TEXT.__dlopen_cstrs: 0xb21
   __TEXT.__ustring: 0x17c
   __TEXT.__swift5_typeref: 0x277f2

   __TEXT.__swift_as_ret: 0x1d4
   __TEXT.__swift5_protos: 0x7c
   __TEXT.__swift5_mpenum: 0x2c
-  __TEXT.__unwind_info: 0x24ef0
+  __TEXT.__unwind_info: 0x24f10
   __TEXT.__eh_frame: 0x6a28
   __TEXT.__objc_classname: 0xb193
-  __TEXT.__objc_methname: 0xfaf2c
-  __TEXT.__objc_methtype: 0x21f8e
+  __TEXT.__objc_methname: 0xfaf40
+  __TEXT.__objc_methtype: 0x21f92
   __TEXT.__objc_stubs: 0x9c7c0
   __DATA_CONST.__got: 0x61e8
   __DATA_CONST.__const: 0xdb38

   __DATA_CONST.__objc_protorefs: 0x3a8
   __DATA_CONST.__objc_superrefs: 0x19c0
   __DATA_CONST.__objc_arraydata: 0x1040
-  __AUTH_CONST.__auth_got: 0x4698
-  __AUTH_CONST.__auth_ptr: 0x34f8
+  __AUTH_CONST.__auth_got: 0x4690
+  __AUTH_CONST.__auth_ptr: 0x35c8
   __AUTH_CONST.__const: 0x27510
-  __AUTH_CONST.__cfstring: 0x242c0
+  __AUTH_CONST.__cfstring: 0x24300
   __AUTH_CONST.__objc_const: 0x8c4a8
   __AUTH_CONST.__objc_arrayobj: 0xea0
   __AUTH_CONST.__objc_intobj: 0x1080

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 55661
+  Functions: 55662
   Symbols:   43664
-  CStrings:  51110
+  CStrings:  51150
 
CStrings:
+ "%s, reason: %@"
+ "%s: balloonView: %@, indexPath: %@"
+ "-[CKChatController _expectedAppCardAndEntryViewHeight]"
+ "-[CKCoreChatController _fullScreenBalloonViewControllerWithChatItem:displayConfiguration:]"
+ "-[CKCoreChatController _handleTapEventForBalloonView:atIndexPath:]"
+ "-[CKCoreChatController fullScreenBalloonViewController:duplicatedViewForChatItem:]"
+ "-[CKCoreChatController fullScreenBalloonViewControllerDidDisappear:]"
+ "-[CKCoreChatController fullScreenBalloonViewControllerHandleDismissTap:]"
+ "-[CKCoreChatController shouldUpdateScrollPositionForKeyboardScreenFrameChanges]"
+ "-[CKCoreChatController showFullScreenAcknowledgmentPickerForChatItem:displayConfiguration:]_block_invoke"
+ "-[CKCoreChatController showFullScreenAcknowledgmentPickerIfNeededForBalloonAtIndexPath:]"
+ "-[CKFullScreenBalloonViewControllerPhone viewDidLayoutSubviews]"
+ "-[CKScrollViewController updateScrollGeometryForReason:withDuration:animationCurve:]"
+ "-[CKScrollViewController updateScrollGeometryWithInheritedAnimationForReason:]"
+ "-[CKScrollViewController updateScrollGeometryWithoutAnimationForReason:]"
+ "-[CKTranscriptCollectionViewController loadEarlierMessages]"
+ "[Tapbacks] %s"
+ "[Tapbacks] %s, : %@ entryView.frame: %@"
+ "[Tapbacks] %s, Presening fullScreenBalloonViewController: no textEffects cancellation in progress, chatItem.guid: %@"
+ "[Tapbacks] %s, _fullScreenBalloonViewController has been set, chatItem.guid: %@"
+ "[Tapbacks] %s, appCardAndEntryViewHeight: %@"
+ "[Tapbacks] %s, balloonViewFrame > %@"
+ "[Tapbacks] %s, chatItem.guid = %@, displayConfiguration: %@"
+ "[Tapbacks] %s, chatItem.guid: %@"
+ "[Tapbacks] %s, chatItem.guid: %@, displayConfiguration: %@"
+ "[Tapbacks] %s, fullScreenBalloonViewController will be presented, chatItem.guid: %@"
+ "[Tapbacks] %s, indexPath: %@"
+ "[Tapbacks] %s, indexPath: %@, proposed chatItem: %@"
+ "[Tapbacks] %s, returning asset snapshot: %@"
+ "[Tapbacks] %s, returning balloonView snapshot: %@"
+ "[Tapbacks] %s, returning balloonView: %@"
+ "[Tapbacks] %s, tapback overlay did disappear for controller: %@"
+ "[Tapbacks] %s, viewDidLayoutSubviews: balloonView > %@"
+ "[Tapbacks] %s, viewDidLayoutSubviews: pickerBalloonParentView > %@"
+ "[Tapbacks] %s: re-routing tap to parent balloon for parentIndexPath: %@, chatItem.guid: %@"
+ "[Tapbacks] %s: tapback overlay %@"
+ "[Tapbacks] %s: tapback overlay %@, at indexPath: %@"
+ "[Tapbacks] Attempted to present ack menu for chat item out of idx range. idx %lu count %lu"
+ "[Tapbacks] Attempting to insert nil sticker"
+ "[Tapbacks] Begin sendTouchBarTapback"
+ "[Tapbacks] Could not find balloonView. This is unexpected."
+ "[Tapbacks] Could not make classic tapback for ack type: %lld"
+ "[Tapbacks] Creating fullscreen balloon for chatItem = %@"
+ "[Tapbacks] Invalid corner width for reply button, width = %f"
+ "[Tapbacks] Invalid reply button size, width = %f, height = %f"
+ "[Tapbacks] Tapback keyboard shortcut invoked for classic tapback but no classic tapbacks loaded in picker"
+ "[Tapbacks] Tapback keyboard shortcut invoked for suggested tapback but no suggested tapbacks loaded in picker"
+ "[Tapbacks] Tapback keyboard shortcut invoked with no TapbackPickerViewController to reference. This is unexpected"
+ "[Tapbacks] Tapback keyboard shortcut invoked with no input"
+ "[Tapbacks] Tapback keyboard shortcut invoked with unsupport int value"
+ "[Tapbacks] Tapback keyboard shortcut invoked with unsupported string value"
+ "[Tapbacks] Tapback picker tried presenting but found nil balloonView"
+ "[Tapbacks] _dismissFullScreenBubbleViewControllerAnimated %@:WithSendAnimation: %d, completion %@"
+ "[Tapbacks] _fullScreenBalloonViewController has been dismissed and set to nil"
+ "[Tapbacks] balloonView minY: %f, topOffset: %f, parentViewY: %f"
+ "[Tapbacks] created tintableBalloon %@"
+ "[Tapbacks] didDeselectTapback: during double-tap"
+ "[Tapbacks] didInsertTapback: Tapback already sent. Will dismiss"
+ "[Tapbacks] didInsertTapback: Tapback not already sent. Will begin sending Tapback"
+ "[Tapbacks] didInsertTapback: completed during double-tap"
+ "[Tapbacks] didSelectTapback: during double-tap"
+ "[Tapbacks] inserting sticker: during double-tap"
+ "[Tapbacks] keyCommandSelectTapback %@"
+ "[Tapbacks] keyboard command invoked while no tapback picker can be referenced"
+ "[Tapbacks] keyboard command sender: %@"
+ "[Tapbacks] not performing closingAnimations: view is currently not presented"
+ "[Tapbacks] not showing tapback attribution: no visible tapbacks"
+ "[Tapbacks] not showing tapback attribution: not message part chatItem"
+ "[Tapbacks] not showing tapback picker: business chat disabled"
+ "[Tapbacks] not showing tapback picker: cannot send to chat"
+ "[Tapbacks] not showing tapback picker: chatItem can't send tapbacks"
+ "[Tapbacks] not showing tapback picker: missing tapbacks chat capability"
+ "[Tapbacks] not showing tapback picker: replies not allowed lock screen"
+ "[Tapbacks] parentBalloonView not found"
+ "[Tapbacks] parentBalloonView: %@"
+ "[Tapbacks] performClosingAnimationsAnimated: %@, WithSendAnimation: %d, withCompletion:%@"
+ "[Tapbacks] shouldShowPicker: %{BOOL}d, shouldShowAttribution: %{BOOL}d, shouldShowFullScreenAcknowledgmentPicker: %{BOOL}d"
+ "[Tapbacks] showTapbackPicker: balloonView is not found. This is unexpected "
+ "[Tapbacks] showTapbackPicker: during double-tap"
+ "[Tapbacks] showTapbackPicker: presenting keyboard input"
+ "[Tapbacks] showTapbackPicker: presenting suggestions selection"
+ "[Tapbacks] unable to generate duplicateView. This is unexpected"
+ "[Tapbacks] verticallyScrollTranscriptByAmount: %@"
+ "[Tapbacks], %s, Ignoring keyboard frame change because full screen balloon view is visible"
+ "[Tapbacks], %s, keyboard frame change allowed"
+ "logSearchResultsReceivedInMode:conversations:tokens:messages:links:photos:location:attachments:wallet:collaboration:highlights:"
+ "not shown"
+ "positioningGuideToActivate: %lu"
+ "shown"
+ "v104@0:8Q16Q24Q32Q40Q48Q56Q64Q72Q80Q88Q96"
- "%s, chatItem.guid: %@"
- "Attempted to present ack menu for chat item out of idx range. idx %lu count %lu"
- "Attempting to insert nil sticker"
- "Begin sendTouchBarTapback"
- "Could not find balloonView. This is unexpected."
- "Could not make classic tapback for ack type: %lld"
- "Creating fullscreen balloon for chatItem = %@"
- "Found balloonView: %@, for chatItem: %@"
- "Ignoring keyboard frame change because full screen balloon view is visible"
- "Invalid corner width for reply button, width = %f"
- "Invalid reply button size, width = %f, height = %f"
- "Presening fullScreenBalloonViewController: no textEffects cancellation in progress, chatItem.guid: %@"
- "Tapback keyboard command invoked while no tapback picker can be referenced"
- "Tapback keyboard shortcut invoked for classic tapback but no classic tapbacks loaded in picker"
- "Tapback keyboard shortcut invoked for suggested tapback but no suggested tapbacks loaded in picker"
- "Tapback keyboard shortcut invoked with no TapbackPickerViewController to reference. This is unexpected"
- "Tapback keyboard shortcut invoked with no input"
- "Tapback keyboard shortcut invoked with unsupport int value"
- "Tapback keyboard shortcut invoked with unsupported string value"
- "Tapback picker tried presenting but found nil balloonView"
- "_appCardHeightWithSafeArea: %@ entryView.frame: %@"
- "_fullScreenBalloonViewController has been dismissed and set to nil"
- "_fullScreenBalloonViewController has been set, chatItem.guid: %@"
- "appCardAndEntryViewHeight: %@"
- "didDeselectTapback: during double-tap"
- "didInsertTapback: Tapback already sent. Will dismiss"
- "didInsertTapback: Tapback not already sent. Will begin sending Tapback"
- "didInsertTapback: completed during double-tap"
- "didSelectTapback: during double-tap"
- "fullScreenBalloonViewController will be presented, chatItem.guid: %@"
- "fullScreenBalloonViewControllerWithChatItem, chatItem = %@"
- "inserting sticker: during double-tap"
- "logSearchResultsReceived:tokens:messages:links:photos:location:attachments:wallet:collaboration:highlights:"
- "not performing closingAnimations: view is currently not presented"
- "not showing tapback attribution: no visible tapbacks"
- "not showing tapback attribution: not message part chatItem"
- "not showing tapback picker: business chat disabled"
- "not showing tapback picker: cannot send to chat"
- "not showing tapback picker: chatItem can't send tapbacks"
- "not showing tapback picker: missing tapbacks chat capability"
- "not showing tapback picker: replies not allowed lock screen"
- "performClosingAnimationsAnimated: %@, WithSendAnimation: %d, withCompletion:%@"
- "showFullScreenAcknowledgmentPickerIfNeededForBalloonAtIndexPath, indexPath: %@"
- "showTapbackPicker: balloonView is not found. This is unexpected "
- "showTapbackPicker: during double-tap"
- "showTapbackPicker: presenting keyboard input"
- "showTapbackPicker: presenting suggestions selection"
- "unable to generate duplicateView. This is unexpected"
- "v96@0:8Q16Q24Q32Q40Q48Q56Q64Q72Q80Q88"
- "verticallyScrollTranscriptByAmount: %@"

```

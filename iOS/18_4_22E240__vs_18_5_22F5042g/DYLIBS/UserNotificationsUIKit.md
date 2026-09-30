## UserNotificationsUIKit

> `/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit`

```diff

-941.5.3.106.0
-  __TEXT.__text: 0x19c080
-  __TEXT.__auth_stubs: 0x24f0
-  __TEXT.__objc_methlist: 0x196a4
-  __TEXT.__const: 0x3644
+941.6.6.101.0
+  __TEXT.__text: 0x19c580
+  __TEXT.__auth_stubs: 0x2500
+  __TEXT.__objc_methlist: 0x196dc
+  __TEXT.__const: 0x3654
   __TEXT.__gcc_except_tab: 0x2d58
-  __TEXT.__cstring: 0xc386
-  __TEXT.__oslogstring: 0xc310
+  __TEXT.__cstring: 0xc366
+  __TEXT.__oslogstring: 0xc848
   __TEXT.__ustring: 0x22
   __TEXT.__swift5_typeref: 0x3de8
   __TEXT.__swift5_fieldmd: 0x1274

   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift5_mpenum: 0x44
-  __TEXT.__unwind_info: 0x6c08
+  __TEXT.__unwind_info: 0x6c18
   __TEXT.__eh_frame: 0xdb0
   __TEXT.__objc_classname: 0x370b
-  __TEXT.__objc_methname: 0x44afc
-  __TEXT.__objc_methtype: 0xbf6f
-  __TEXT.__objc_stubs: 0x27b00
+  __TEXT.__objc_methname: 0x44bb9
+  __TEXT.__objc_methtype: 0xbf8e
+  __TEXT.__objc_stubs: 0x27b20
   __DATA_CONST.__got: 0x1728
-  __DATA_CONST.__const: 0x4098
+  __DATA_CONST.__const: 0x4090
   __DATA_CONST.__objc_classlist: 0x7b0
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x5e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc330
+  __DATA_CONST.__objc_selrefs: 0xc348
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x550
   __DATA_CONST.__objc_arraydata: 0x158
-  __AUTH_CONST.__auth_got: 0x1288
-  __AUTH_CONST.__auth_ptr: 0x798
+  __AUTH_CONST.__auth_got: 0x1290
+  __AUTH_CONST.__auth_ptr: 0x790
   __AUTH_CONST.__const: 0x5168
-  __AUTH_CONST.__cfstring: 0x7d00
-  __AUTH_CONST.__objc_const: 0x24738
+  __AUTH_CONST.__cfstring: 0x7ce0
+  __AUTH_CONST.__objc_const: 0x24768
   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x2590
   __AUTH.__data: 0x728
-  __DATA.__objc_ivar: 0x1628
+  __DATA.__objc_ivar: 0x162c
   __DATA.__data: 0x50f0
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x1a50

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10255
-  Symbols:   9485
-  CStrings:  12387
+  Functions: 10259
+  Symbols:   9489
+  CStrings:  12394
 
Symbols:
+ _os_transaction_create
- _NCNotificationListDisplayStyleReasonSensitiveUIDisabled
CStrings:
+ "\x01!\x1f\f!"
+ "%{public}s added, scroll to systemPreferred %{public}s"
+ "%{public}s: add(portal:,background:) couldn't add portal %{public}s or background %{public}s; window is %{public}s; portalContainer.window is %{public}s; backgroundContainer.window is %{public}s; dropletContextView.window is %{public}s"
+ "%{public}s: addOrRemovePortalsIfAppropriate() not adding portals; backgroundContainer.window is %{public}s; dropletContextView.window is %{public}s"
+ "%{public}s: added to window %{public}s"
+ "%{public}s: createDroplet(for:) adding portal %{public}s and background %{public}s"
+ "%{public}s: removeDroplet(_:) removing portal %{public}s and background %{public}s"
+ "%{public}s: removed from window"
+ "@\"NSObject<OS_os_transaction>\""
+ "Acquiring backlight assertion with reason %{public}s"
+ "Backlight assertion %{public}s acquired"
+ "Backlight assertion %{public}s cancelled without error"
+ "Backlight assertion %{public}s failed to acquired with error: %{public}@"
+ "Backlight assertion %{public}s is cancelled with error: %{public}@"
+ "Backlight assertion is already acquired with %{public}s"
+ "Backlight changed from %{public}ld to %{public}ld"
+ "Calculated exclusionZones: %{public}s"
+ "Calculated pages: %{public}s"
+ "Cannot get any page for display style - %{public}ld; currentPages - %{public}s; scroll to 0.0"
+ "Changed scroll state: %{public}s"
+ "Content changed. Recalculated pages: %{public}s, scrollState: %{public}s, exclusionZones: %{public}s, currentPosition: %{public}s"
+ "ContentSizeCategory changed, scroll to systemPreferredPageType %{public}s"
+ "Count indicator did tap, scroll to %{public}s"
+ "CountIndicatorViewController updating count indicator with displayStyleSettingEnum: %{public}ld; count %{public}ld; title %{public}s"
+ "CurrentOffset %{public}f is within targetPage %{public}s. Stop scrolling."
+ "DND mode %{public}s toggled; missedSectionActive: %{bool,public}d; hideVisibleNotifications: %{bool,public}d"
+ "Did change authentication status: %{bool,public}d, isUserEngagingView %{bool,public}d"
+ "Did immediate layout for supplement: %{public}@. Supplement height: %{public}f"
+ "Display style did change for sleep, new systemPreferredPageType %{public}s, reason: %{public}s"
+ "Doesn't remove notification from any sections; skip scrolling for %{public}s removal"
+ "ExclusionManager scroll to the zoneIndex %{public}ld doesn't belong to any page."
+ "Expand ground %{public}s"
+ "Failed to send feedback: %{public}@"
+ "Failed to send priority feedback: %{public}@"
+ "GroupList %{public}s set grouped to %{bool,public}d"
+ "Hit an exclusion zone at index %{public}ld that has no associated page, and we jumped here"
+ "Hit an exclusion zone at index %{public}ld that has no associated page, ignoring scroll event"
+ "In landscape mode scroll can't lower than List.minY, limitContentOffset to: %{public}f."
+ "Incoming revealed: %{bool,public}d, History revealed: %{bool,public}d"
+ "It's not alerting request; scroll to systemPreferred %{public}s (reason: %{public}s) for %{public}s insertion"
+ "Modify %{public}s"
+ "No backlight changed for %{public}ld; skip scroll position update"
+ "Page is empty; scroll to top for %{public}s removal"
+ "Page was empty before insert below the fold, scroll to %{public}s for %{public}s insertion"
+ "Persistent and Incoming section not found! persistentIndex: %{public}ld); incomingIndex: %{public}ld"
+ "Previous systemSettings is nil; force updating scroll position and pageType to %{public}s"
+ "Received feedback with action %{public}s"
+ "Releasing backlight assertion with reason %{public}s"
+ "Remove %{public}s"
+ "Scroll down after new incoming changed, system preferred %{public}s <= %{public}s with reason %{public}s, scroll to %{public}s"
+ "Scroll lower than Count.minY, limitContentOffset to: %{public}f."
+ "Scroll over lastPage %{public}s maxY, limitContentOffset to %{public}f."
+ "Scroll position is valid: %{bool,public}d"
+ "Scroll state changed to: %{public}s"
+ "Scroll to SystemPreferred %{public}s (reason: %{public}s) in AOD;"
+ "Scroll to systemPreferred %{public}s in full backlight (reason: %{public}s)"
+ "Scroll to to targetPage: %{public}s minY with holdToPage request %{public}s, currentOffset: %{public}f"
+ "ScrollView did end decelerating: %{public}f"
+ "ScrollView did end dragging: %{public}f"
+ "ScrollView did end scrolling animation: %{public}f"
+ "ScrollView did scroll %{public}f"
+ "ScrollView end decelerating in transition page with percentage %{public}f, previousPage: %{public}s, nextPage: %{public}s. Re-validate scrollPosition"
+ "ScrollView will end dragging on %{public}f"
+ "Scrolling to page: %{public}s %{public}s: %{public}f"
+ "SectionList %{public}s set grouped to %{bool,public}d"
+ "Setting content offset without animation: %{public}f"
+ "Skip scroll to systemPreferred in full backlight, already in systemPreferredPageType %{public}s (reason: %{public}s)"
+ "Skip scrollView requesting scrollToTop; currentPageType is %{public}s not .list"
+ "Still have %{public}ld assertions to complete; Not releasing backlight assertion"
+ "Supplementary section did change content: %{public}@. Supplement height: %{public}f. isUserEngagingView: %{bool,public}d"
+ "Supplementary section did change height: %{public}@. Supplement height: %{public}f."
+ "SupplementaryViewsGroup %{public}s set grouped to %{bool,public}d"
+ "T@\"NSObject<OS_os_transaction>\",&,N,V_manyNotificationsTransaction"
+ "Unable to find page for targetPageType %{public}s"
+ "Unexpected position %{public}s"
+ "Unknown group found %{public}s! Better to double check for scroll position integrity."
+ "User is engaging, skip scrolling for %{public}s insertion"
+ "User is engaging, skip update scroll position for %{public}s added"
+ "User tap on %{public}s; incomingCount %{public}ld; currentPageType %{public}s"
+ "Verifying scroll position... Current offset: %{public}f"
+ "_backlightLuminance is %{public}ld; skip scrolling for %{public}s removal"
+ "_manyNotificationsTransaction"
+ "_updateTransactionIfNecessary"
+ "highlights isn't settled enough; scroll to %{public}s; expandedPercentage %{public}f; _backlightLuminance %{public}ld"
+ "interfaceSizeClass changes to %{public}ld in AOD; updating scroll position"
+ "interfaceSizeClass changes to %{public}ld in CoverSheet; updating pages"
+ "interfaceSizeClass is not changed; currentInterfaceSizeClass %{public}ld"
+ "isNotificationHistoryRevealed: %{bool,public}d, scroll to .list"
+ "isUserEngagingView true; _backlightLuminance: %{public}ld; systemPreferredPageType: %{public}s; currentPageType: %{public}s"
+ "manyNotificationsTransaction"
+ "setManyNotificationsTransaction:"
+ "setNeedsScroll %{public}s"
+ "targetScrollPosition: %{public}s, scrollState: %{public}s, viewEffectivelyTracking: %{bool,public}d, _backlightLuminance: %{public}ld"
- "\x01!\x1f\v!"
- "%s added, scroll to systemPreferred %s"
- "%s: add(portal:,background:) couldn't add portal %s or background %s; window is %s; portalContainer.window is %s; backgroundContainer.window is %s; dropletContextView.window is %s"
- "%s: addOrRemovePortalsIfAppropriate() not adding portals; backgroundContainer.window is %s; dropletContextView.window is %s"
- "%s: added to window %s"
- "%s: createDroplet(for:) adding portal %s and background %s"
- "%s: removeDroplet(_:) removing portal %s and background %s"
- "%s: removed from window"
- "Acquiring backlight assertion with reason %s"
- "Backlight assertion %s acquired"
- "Backlight assertion %s cancelled without error"
- "Backlight assertion %s failed to acquired with error: %@"
- "Backlight assertion %s is cancelled with error: %@"
- "Backlight assertion is already acquired with %s"
- "Backlight changed from %ld to %ld"
- "Calculated exclusionZones: %s"
- "Calculated pages: %s"
- "Cannot get any page for display style - %{public}ld; currentPages - %s; scroll to 0.0"
- "Changed scroll state: %s"
- "Content changed. Recalculated pages: %s, scrollState: %s, exclusionZones: %s, currentPosition: %s"
- "ContentSizeCategory changed, scroll to systemPreferredPageType %s"
- "Count indicator did tap, scroll to %s"
- "CountIndicatorViewController updating count indicator with displayStyleSettingEnum: %ld; count %ld; title %s"
- "CurrentOffset %f is within targetPage %s. Stop scrolling."
- "DND mode %s toggled; missedSectionActive: %{bool}d; hideVisibleNotifications: %{bool}d"
- "Did change authentication status: %{bool}d, isUserEngagingView %{bool}d"
- "Did immediate layout for supplement: %@. Supplement height: %f"
- "Doesn't remove notification from any sections; skip scrolling for %s removal"
- "ExclusionManager scroll to the zoneIndex %ld doesn't belong to any page."
- "Expand ground %s"
- "Failed to send feedback: %@"
- "Failed to send priority feedback: %@"
- "GroupList %s set grouped to %{bool}d"
- "Hit an exclusion zone at index %ld that has no associated page, and we jumped here"
- "Hit an exclusion zone at index %ld that has no associated page, ignoring scroll event"
- "In landscape mode scroll can't lower than List.minY, limitContentOffset to: %f."
- "Incoming revealed: %{bool}d, History revealed: %{bool}d"
- "It's not alerting request; scroll to systemPreferred %s (reason: %s) for %s insertion"
- "Modify %s"
- "NCNotificationListDisplayStyleReasonSensitiveUIDisabled"
- "No backlight changed for %ld; skip scroll position update"
- "Page is empty; scroll to top for %s removal"
- "Page was empty before insert below the fold, scroll to %s for %s insertion"
- "Persistent and Incoming section not found! persistentIndex: %ld); incomingIndex: %ld"
- "Previous systemSettings is nil; force updating scroll position and pageType to %s"
- "Received feedback with action %s"
- "Releasing backlight assertion with reason %s"
- "Remove %s"
- "Scroll down after new incoming changed, system preferred %s <= %s with reason %s, scroll to %s"
- "Scroll lower than Count.minY, limitContentOffset to: %f."
- "Scroll over lastPage %s maxY, limitContentOffset to %f."
- "Scroll position is valid: %{bool}d"
- "Scroll state changed to: %s"
- "Scroll to SystemPreferred %s (reason: %s) in AOD;"
- "Scroll to systemPreferred %s in full backlight (reason: %s)"
- "Scroll to to targetPage: %s minY with holdToPage request %s, currentOffset: %f"
- "ScrollView did end decelerating: %f"
- "ScrollView did end dragging: %f"
- "ScrollView did end scrolling animation: %f"
- "ScrollView did scroll %f"
- "ScrollView end decelerating in transition page with percentage %f, previousPage: %s, nextPage: %s. Re-validate scrollPosition"
- "ScrollView will end dragging on %f"
- "Scrolling to page: %s %s: %f"
- "SectionList %s set grouped to %{bool}d"
- "Setting content offset without animation: %f"
- "Skip scroll to systemPreferred in full backlight, already in systemPreferredPageType %s (reason: %s)"
- "Skip scrollView requesting scrollToTop; currentPageType is %s not .list"
- "Still have %ld assertions to complete; Not releasing backlight assertion"
- "Supplementary section did change content: %@. Supplement height: %f. isUserEngagingView: %{bool}d"
- "Supplementary section did change height: %@. Supplement height: %f."
- "SupplementaryViewsGroup %s set grouped to %{bool}d"
- "Unable to find page for targetPageType %s"
- "Unexpected position %s"
- "Unknown group found %s! Better to double check for scroll position integrity."
- "User is engaging, skip scrolling for %s insertion"
- "User is engaging, skip update scroll position for %s added"
- "User tap on %s; incomingCount %ld; currentPageType %s"
- "Verifying scroll position... Current offset: %f"
- "_backlightLuminance is %ld; skip scrolling for %s removal"
- "highlights isn't settled enough; scroll to %s; expandedPercentage %f; _backlightLuminance %ld"
- "interfaceSizeClass changes to %ld in AOD; updating scroll position"
- "interfaceSizeClass changes to %ld in CoverSheet; updating pages"
- "interfaceSizeClass is not changed; currentInterfaceSizeClass %ld"
- "isNotificationHistoryRevealed: %{bool}d, scroll to .list"
- "isUserEngagingView true; _backlightLuminance: %ld; systemPreferredPageType: %s; currentPageType: %s"
- "setNeedsScroll %s"
- "targetScrollPosition: %s, scrollState: %s, viewEffectivelyTracking: %{bool}d, _backlightLuminance: %ld"

```

## CompanionAppViewSetup

> `/System/Library/AccessibilityBundles/CompanionAppViewSetup.axbundle/CompanionAppViewSetup`

```diff

-2909.1.4.3.0
-  __TEXT.__text: 0x480
-  __TEXT.__auth_stubs: 0x120
-  __TEXT.__objc_methlist: 0x74
-  __TEXT.__cstring: 0x11a
-  __TEXT.__unwind_info: 0x78
-  __TEXT.__objc_classname: 0x77
-  __TEXT.__objc_methname: 0x2a5
-  __TEXT.__objc_methtype: 0x33
-  __TEXT.__objc_stubs: 0x240
-  __DATA_CONST.__got: 0x8
-  __DATA_CONST.__const: 0x60
-  __DATA_CONST.__objc_classlist: 0x18
+2909.1.4.13.0
+  __TEXT.__text: 0x30d4
+  __TEXT.__auth_stubs: 0x340
+  __TEXT.__objc_methlist: 0x254
+  __TEXT.__cstring: 0xfae
+  __TEXT.__const: 0x10
+  __TEXT.__gcc_except_tab: 0x28
+  __TEXT.__unwind_info: 0x130
+  __TEXT.__objc_classname: 0x12a
+  __TEXT.__objc_methname: 0x9ee
+  __TEXT.__objc_methtype: 0x10a
+  __TEXT.__objc_stubs: 0x8a0
+  __DATA_CONST.__got: 0x30
+  __DATA_CONST.__const: 0x188
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xd8
-  __DATA_CONST.__objc_selrefs: 0xb8
-  __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x180
-  __AUTH_CONST.__objc_const: 0xd8
-  __AUTH_CONST.__auth_got: 0x98
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_classrefs: 0x30
-  __DATA.__objc_superrefs: 0x8
-  __DATA.__bss: 0x10
+  __DATA_CONST.__objc_const: 0x1f8
+  __DATA_CONST.__objc_selrefs: 0x2f0
+  __AUTH_CONST.__const: 0xe0
+  __AUTH_CONST.__cfstring: 0x1700
+  __AUTH_CONST.__objc_const: 0x1f8
+  __AUTH_CONST.__auth_got: 0x1b0
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_classrefs: 0x60
+  __DATA.__objc_superrefs: 0x18
+  __DATA.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
+  - /System/Library/PrivateFrameworks/AppConduit.framework/AppConduit
+  - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility
   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5DC3C2A0-A39E-36ED-AED9-07C9E199D53E
-  Functions: 12
-  Symbols:   96
-  CStrings:  60
+  UUID: 65A79A7D-C253-3290-9A03-7968652EE244
+  Functions: 60
+  Symbols:   330
+  CStrings:  507
 
Symbols:
+ +[CSLUIFieldOfIconsViewAccessibility _accessibilityPerformValidations:]
+ +[CSLUIFieldOfIconsViewAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[CSLUIFieldOfIconsViewAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[CSLUINanoResourceGrabberIconViewAccessibility _accessibilityPerformValidations:]
+ +[CSLUINanoResourceGrabberIconViewAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[CSLUINanoResourceGrabberIconViewAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[CSLUIFieldOfIconsViewAccessibility _accessibilityAnnounceUpdatedPositionForElement:]
+ -[CSLUIFieldOfIconsViewAccessibility _accessibilityHitTestShouldFallbackToNearestChild]
+ -[CSLUIFieldOfIconsViewAccessibility _accessibilityHitTestSubviews]
+ -[CSLUIFieldOfIconsViewAccessibility _accessibilityIsScrollAncestor]
+ -[CSLUIFieldOfIconsViewAccessibility _accessibilityLoadAccessibilityInformation]
+ -[CSLUIFieldOfIconsViewAccessibility _accessibilityMoveElement:left:]
+ -[CSLUIFieldOfIconsViewAccessibility _accessibilityMoveIconLeft:]
+ -[CSLUIFieldOfIconsViewAccessibility _accessibilityMoveIconRight:]
+ -[CSLUIFieldOfIconsViewAccessibility _accessibilityScrollSize]
+ -[CSLUIFieldOfIconsViewAccessibility _accessibilityScrollToChild:animated:]
+ -[CSLUIFieldOfIconsViewAccessibility _accessibilityStartJiggleMode:]
+ -[CSLUIFieldOfIconsViewAccessibility _axHexForIconView:]
+ -[CSLUIFieldOfIconsViewAccessibility _axUpdateIconElements]
+ -[CSLUIFieldOfIconsViewAccessibility accessibilityElements]
+ -[CSLUIFieldOfIconsViewAccessibility accessibilityIdentifier]
+ -[CSLUIFieldOfIconsViewAccessibility accessibilityScrollDownPage]
+ -[CSLUIFieldOfIconsViewAccessibility accessibilityScrollToVisibleWithChild:]
+ -[CSLUIFieldOfIconsViewAccessibility accessibilityScrollUpPage]
+ -[CSLUIFieldOfIconsViewAccessibility addedNodes:]
+ -[CSLUIFieldOfIconsViewAccessibility attemptBeginDraggingNode:fromPoint:]
+ -[CSLUIFieldOfIconsViewAccessibility beginDraggingView:atPoint:node:]
+ -[CSLUIFieldOfIconsViewAccessibility dragToPoint:translation:]
+ -[CSLUIFieldOfIconsViewAccessibility hexAppGraph:addedNodes:removedNodes:movedNodes:]
+ -[CSLUIFieldOfIconsViewAccessibility loadIconViews]
+ -[CSLUIFieldOfIconsViewAccessibility removedNodes:]
+ -[CSLUIFieldOfIconsViewAccessibility revealViews:]
+ -[CSLUIFieldOfIconsViewAccessibility setLayout:percentComplete:animated:options:]
+ -[CSLUINanoResourceGrabberIconViewAccessibility accessibilityLabel]
+ -[CSLUINanoResourceGrabberIconViewAccessibility accessibilityPath]
+ -[CSLUINanoResourceGrabberIconViewAccessibility isAccessibilityElement]
+ GCC_except_table12
+ GCC_except_table8
+ _AXAppNameForBundleId
+ _AXIsInternalInstall
+ _AXPerformSafeBlock
+ _AXSafeClassFromString
+ _AX_CGRectGetCenter
+ _CFAbsoluteTimeGetCurrent
+ _CGRectContainsPoint
+ _NSSelectorFromString
+ _OBJC_CLASS_$_CSLUIFieldOfIconsViewAccessibility
+ _OBJC_CLASS_$_CSLUINanoResourceGrabberIconViewAccessibility
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_UIAccessibilityCustomAction
+ _OBJC_CLASS_$___CSLUIFieldOfIconsViewAccessibility_super
+ _OBJC_CLASS_$___CSLUINanoResourceGrabberIconViewAccessibility_super
+ _OBJC_METACLASS_$_CSLUIFieldOfIconsViewAccessibility
+ _OBJC_METACLASS_$_CSLUINanoResourceGrabberIconViewAccessibility
+ _OBJC_METACLASS_$___CSLUIFieldOfIconsViewAccessibility_super
+ _OBJC_METACLASS_$___CSLUINanoResourceGrabberIconViewAccessibility_super
+ _UIAccessibilityAnnouncementNotification
+ _UIAccessibilityIsVoiceOverRunning
+ _UIAccessibilityLayoutChangedNotification
+ _UIAccessibilityPostNotification
+ __AXAssert
+ __Block_object_dispose
+ __NSConcreteStackBlock
+ __OBJC_$_CLASS_METHODS_CSLUIFieldOfIconsViewAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS_CSLUINanoResourceGrabberIconViewAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_CSLUIFieldOfIconsViewAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_CSLUINanoResourceGrabberIconViewAccessibility(SafeCategory)
+ __OBJC_CLASS_RO_$_CSLUIFieldOfIconsViewAccessibility
+ __OBJC_CLASS_RO_$_CSLUINanoResourceGrabberIconViewAccessibility
+ __OBJC_CLASS_RO_$___CSLUIFieldOfIconsViewAccessibility_super
+ __OBJC_CLASS_RO_$___CSLUINanoResourceGrabberIconViewAccessibility_super
+ __OBJC_METACLASS_RO_$_CSLUIFieldOfIconsViewAccessibility
+ __OBJC_METACLASS_RO_$_CSLUINanoResourceGrabberIconViewAccessibility
+ __OBJC_METACLASS_RO_$___CSLUIFieldOfIconsViewAccessibility_super
+ __OBJC_METACLASS_RO_$___CSLUINanoResourceGrabberIconViewAccessibility_super
+ __Unwind_Resume
+ ___59-[CSLUIFieldOfIconsViewAccessibility _axUpdateIconElements]_block_invoke
+ ___62-[CSLUIFieldOfIconsViewAccessibility dragToPoint:translation:]_block_invoke
+ ___62-[CSLUIFieldOfIconsViewAccessibility dragToPoint:translation:]_block_invoke_2
+ ___63-[CSLUIFieldOfIconsViewAccessibility accessibilityScrollUpPage]_block_invoke
+ ___63-[CSLUIFieldOfIconsViewAccessibility accessibilityScrollUpPage]_block_invoke_2
+ ___63-[CSLUIFieldOfIconsViewAccessibility accessibilityScrollUpPage]_block_invoke_3
+ ___65-[CSLUIFieldOfIconsViewAccessibility accessibilityScrollDownPage]_block_invoke
+ ___65-[CSLUIFieldOfIconsViewAccessibility accessibilityScrollDownPage]_block_invoke_2
+ ___67-[CSLUINanoResourceGrabberIconViewAccessibility accessibilityLabel]_block_invoke
+ ___69-[CSLUIFieldOfIconsViewAccessibility _accessibilityMoveElement:left:]_block_invoke
+ ___69-[CSLUIFieldOfIconsViewAccessibility _accessibilityMoveElement:left:]_block_invoke_2
+ ___75-[CSLUIFieldOfIconsViewAccessibility _accessibilityScrollToChild:animated:]_block_invoke
+ ___UIAXStringForVariables
+ ___block_descriptor_32_e25_B24?08"NSDictionary"16l
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e15_v32?08Q16^B24l
+ ___block_descriptor_40_e8_32s_e11_q24?0816ls32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s_e5_v8?0ls32l8
+ ___block_literal_global.460
+ ___objc_personality_v0
+ ___stack_chk_fail
+ ___stack_chk_guard
+ _accessibilityLabel.Labels
+ _accessibilityLabel.onceToken
+ _dispatch_once
+ _dragToPoint:translation:.ClockClass
+ _dragToPoint:translation:.ClockElement
+ _dragToPoint:translation:.LastClockTimeRetrieval
+ _dragToPoint:translation:.LastProcessTime
+ _dragToPoint:translation:.LastString
+ _dragToPoint:translation:.onceToken
+ _kAXPerformElementUpdateImmediatelyToken
+ _objc_alloc
+ _objc_enumerationMutation
+ _objc_msgSend$_accessibilityAnnounceUpdatedPositionForElement:
+ _objc_msgSend$_accessibilityCirclePathBasedOnBoundsWidth
+ _objc_msgSend$_accessibilityFirstElementForFocus
+ _objc_msgSend$_accessibilityIsRTL
+ _objc_msgSend$_accessibilityMoveElement:left:
+ _objc_msgSend$_accessibilityScrollSize
+ _objc_msgSend$_accessibilityScrollToChild:animated:
+ _objc_msgSend$_accessibilitySetAssignedValue:forKey:
+ _objc_msgSend$_accessibilitySetRetainedValue:forKey:
+ _objc_msgSend$_accessibilityValueForKey:
+ _objc_msgSend$_axHexForIconView:
+ _objc_msgSend$_axUpdateIconElements
+ _objc_msgSend$_setAccessibilityServesAsFirstElement:
+ _objc_msgSend$accessibilityElements
+ _objc_msgSend$accessibilityScrollToVisibleWithChild:
+ _objc_msgSend$addDragDelta:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$allValues
+ _objc_msgSend$array
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$axSafelyAddObject:
+ _objc_msgSend$bounds
+ _objc_msgSend$contentOffsetToCenterHex:
+ _objc_msgSend$convertPoint:fromView:
+ _objc_msgSend$convertPoint:toView:
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$filteredArrayUsingPredicate:
+ _objc_msgSend$indexOfObject:
+ _objc_msgSend$inertialUpdater:willDecelerateWithTarget:
+ _objc_msgSend$initWithName:target:selector:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$length
+ _objc_msgSend$moveNode:toHex:final:
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$safeBoolForKey:
+ _objc_msgSend$safeCGPointForKey:
+ _objc_msgSend$safeIvarForKey:
+ _objc_msgSend$setAccessibilityCustomActions:
+ _objc_msgSend$setContentOffset:animated:
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$subviews
+ _objc_msgSend$validateClass:
+ _objc_msgSend$validateClass:conformsToProtocol:
+ _objc_msgSend$validateProtocol:hasMethod:isInstanceMethod:isRequired:
+ _objc_opt_respondsToSelector
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x9
+ _objc_retain_x19
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x27
+ _objc_storeStrong
+ _objc_unsafeClaimAutoreleasedReturnValue
CStrings:
+ "-[CSLUINanoResourceGrabberIconViewAccessibility accessibilityLabel]"
+ "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles/CarouselAppViewSettingsAccessibility/CSLUINanoResourceGrabberIconViewAccessibility.m"
+ "<CSLUIHexIconActionDelegate>"
+ "@"
+ "@24@0:8@16"
+ "AccessibilityElementsKey"
+ "B"
+ "B24@0:8@16"
+ "B24@?0@8@\"NSDictionary\"16"
+ "B28@0:8@16B24"
+ "CSLHexAppGraph"
+ "CSLHexAppNode"
+ "CSLHexLayout"
+ "CSLInterpolatedHexLayout"
+ "CSLLauncherView"
+ "CSLUIFieldOfIconsView"
+ "CSLUIFieldOfIconsViewAccessibility"
+ "CSLUIHexIconActionDelegate"
+ "CSLUIIconView"
+ "CSLUIInertialUpdater"
+ "CSLUILauncherStyleButtonView"
+ "CSLUINanoResourceGrabberIconView"
+ "CSLUINanoResourceGrabberIconViewAccessibility"
+ "Internal only, missing app name: %@"
+ "Missing app name: %@"
+ "NCClockIconView"
+ "NSString"
+ "PUICCrownInputSequencerDelegate"
+ "Q"
+ "UIView"
+ "UIView<CSLUIHexIconView>"
+ "_UIFocusEnvironmentPrivate"
+ "__AXStringForVariablesSentinel"
+ "__CSLUIFieldOfIconsViewAccessibility_super"
+ "__CSLUINanoResourceGrabberIconViewAccessibility_super"
+ "_accessibilityAnnounceUpdatedPositionForElement:"
+ "_accessibilityCirclePathBasedOnBoundsWidth"
+ "_accessibilityFirstElementForFocus"
+ "_accessibilityHitTestShouldFallbackToNearestChild"
+ "_accessibilityHitTestSubviews"
+ "_accessibilityIsRTL"
+ "_accessibilityIsScrollAncestor"
+ "_accessibilityLoadAccessibilityInformation"
+ "_accessibilityMoveElement:left:"
+ "_accessibilityMoveIconLeft:"
+ "_accessibilityMoveIconRight:"
+ "_accessibilityScrollSize"
+ "_accessibilityScrollToChild:animated:"
+ "_accessibilitySetAssignedValue:forKey:"
+ "_accessibilitySetRetainedValue:forKey:"
+ "_accessibilityStartJiggleMode:"
+ "_accessibilityValueForKey:"
+ "_actionDelegate"
+ "_axHexForIconView:"
+ "_axUpdateIconElements"
+ "_bundleID"
+ "_contentOffset"
+ "_contentView"
+ "_didPanDrag"
+ "_dragView"
+ "_endLayout"
+ "_hex"
+ "_iconGraph"
+ "_iconViewDict"
+ "_inertialUpdater"
+ "_layout"
+ "_linearFocusMovementSequences"
+ "_listViewButtonView"
+ "_pressedIcon"
+ "_setAccessibilityServesAsFirstElement:"
+ "accessibilityElements"
+ "accessibilityIdentifier"
+ "accessibilityPath"
+ "accessibilityScrollDownPage"
+ "accessibilityScrollToVisibleWithChild:"
+ "accessibilityScrollUpPage"
+ "addDragDelta:"
+ "addObjectsFromArray:"
+ "addedNodes:"
+ "allValues"
+ "app.activity"
+ "app.alarm"
+ "app.appstore"
+ "app.bloodoxygen"
+ "app.books"
+ "app.breathe"
+ "app.calculator"
+ "app.camera"
+ "app.compass"
+ "app.connect"
+ "app.contacts"
+ "app.cycletracking"
+ "app.ecg"
+ "app.finddevices"
+ "app.finditems"
+ "app.findmy"
+ "app.findpeople"
+ "app.heartrate"
+ "app.home"
+ "app.mail"
+ "app.maps"
+ "app.medications"
+ "app.memoji"
+ "app.messages"
+ "app.mind"
+ "app.move.left"
+ "app.move.right"
+ "app.moved.after"
+ "app.moved.before"
+ "app.music"
+ "app.news"
+ "app.noise"
+ "app.nowplaying"
+ "app.passbook"
+ "app.phone"
+ "app.photos"
+ "app.podcasts"
+ "app.reminders"
+ "app.remote"
+ "app.sessiontracker"
+ "app.settings"
+ "app.shortcuts"
+ "app.sleep"
+ "app.stocks"
+ "app.stopwatch"
+ "app.taptoradar"
+ "app.timer"
+ "app.tips"
+ "app.voicememos"
+ "app.walkietalkie"
+ "app.weather"
+ "app.world.clock"
+ "apps.arrange"
+ "array"
+ "arrayWithObjects:count:"
+ "attemptBeginDraggingNode: fromPoint:"
+ "attemptBeginDraggingNode:fromPoint:"
+ "axSafelyAddObject:"
+ "beginDraggingView: atPoint: node:"
+ "beginDraggingView:atPoint:node:"
+ "bounds"
+ "centeredHex"
+ "com.apple.ActivityMonitorApp"
+ "com.apple.AppStore"
+ "com.apple.DeepBreathing"
+ "com.apple.HeartRate"
+ "com.apple.Mind"
+ "com.apple.MobileSMS"
+ "com.apple.NanoAlarm"
+ "com.apple.NanoBooks"
+ "com.apple.NanoCalculator.watchkitapp"
+ "com.apple.NanoCamera"
+ "com.apple.NanoCompass.watchkitapp"
+ "com.apple.NanoContacts"
+ "com.apple.NanoHeartRhythm"
+ "com.apple.NanoHome"
+ "com.apple.NanoMail"
+ "com.apple.NanoMaps"
+ "com.apple.NanoMedications"
+ "com.apple.NanoMenstrualCycles"
+ "com.apple.NanoMusic"
+ "com.apple.NanoNowPlaying"
+ "com.apple.NanoOxygenSaturation.watchkitapp"
+ "com.apple.NanoPassbook"
+ "com.apple.NanoPhone"
+ "com.apple.NanoPhotos"
+ "com.apple.NanoReminders"
+ "com.apple.NanoRemote"
+ "com.apple.NanoSettings"
+ "com.apple.NanoSleep.watchkitapp"
+ "com.apple.NanoStopwatch"
+ "com.apple.NanoTapToRadar"
+ "com.apple.NanoTips"
+ "com.apple.NanoWorldClock"
+ "com.apple.Noise"
+ "com.apple.SessionTrackerApp"
+ "com.apple.TapToRadar.watchkitapp"
+ "com.apple.VoiceMemos"
+ "com.apple.findmy"
+ "com.apple.findmy.finddevices"
+ "com.apple.findmy.finditems"
+ "com.apple.findmy.findpeople"
+ "com.apple.ist.AppleConnect.watchkitapp"
+ "com.apple.nanonews"
+ "com.apple.podcasts"
+ "com.apple.private.NanoTimer"
+ "com.apple.shortcuts.watch"
+ "com.apple.stocks.watchapp"
+ "com.apple.tincan"
+ "com.apple.watchmemojieditor"
+ "com.apple.weather.gizmoapp"
+ "com.apple.weather.watchapp"
+ "commitMove"
+ "contentOffsetToCenterHex:"
+ "convertPoint:fromView:"
+ "convertPoint:toView:"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "crownInputSequencerDidBecomeIdle:willDecelerate:"
+ "d"
+ "dictionaryWithObjects:forKeys:count:"
+ "didUpdateFocusInContext:withAnimationCoordinator:"
+ "dragToPoint:translation:"
+ "element.to.the.left.of"
+ "element.to.the.right.of"
+ "enumerateObjectsUsingBlock:"
+ "filteredArrayUsingPredicate:"
+ "handleLongPress"
+ "handlePanGesture:"
+ "hex"
+ "hexAppGraph: addedNodes: removedNodes: movedNodes:"
+ "hexAppGraph:addedNodes:removedNodes:movedNodes:"
+ "iconViewAtHexPoint:"
+ "indexOfObject:"
+ "inertialUpdater:willDecelerateWithTarget:"
+ "initWithName:target:selector:"
+ "isEditing"
+ "isEqualToString:"
+ "kAXOwningElement"
+ "length"
+ "loadIconViews"
+ "moveNode: toHex: final:"
+ "moveNode:toHex:final:"
+ "mutableCopy"
+ "node"
+ "objectAtIndex:"
+ "objectForKey:"
+ "percentComplete"
+ "predicateWithBlock:"
+ "q24@?0@8@16"
+ "region.lower.left"
+ "region.lower.right"
+ "region.upper.left"
+ "region.upper.right"
+ "removedNodes:"
+ "revealViews:"
+ "safeBoolForKey:"
+ "safeCGPointForKey:"
+ "safeIvarForKey:"
+ "setAccessibilityCustomActions:"
+ "setContentOffset:animated:"
+ "setLayout: percentComplete: animated: options:"
+ "setLayout:percentComplete:animated:options:"
+ "sortedArrayUsingComparator:"
+ "started.moving.app"
+ "stringWithFormat:"
+ "subviews"
+ "updateWithCrownInputEvent:"
+ "v"
+ "v28@0:8@16B24"
+ "v32@?0@8Q16^B24"
+ "v40@0:8@16{CGPoint=dd}24"
+ "v44@0:8@16d24B32Q36"
+ "v48@0:8@16@24@32@40"
+ "v48@0:8@16{CGPoint=dd}24@40"
+ "v48@0:8{CGPoint=dd}16{CGPoint=dd}32"
+ "v8@?0"
+ "validateClass:"
+ "validateClass:conformsToProtocol:"
+ "validateProtocol:hasMethod:isInstanceMethod:isRequired:"
+ "{CGPoint=dd}"
+ "{CGSize=dd}16@0:8"
+ "{Hex=ii}"
+ "{Hex=ii}24@0:8@16"

```

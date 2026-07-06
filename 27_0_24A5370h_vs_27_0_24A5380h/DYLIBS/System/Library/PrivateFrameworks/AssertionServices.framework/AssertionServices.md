## AssertionServices

> `/System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices`

Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Functions:
~ -[BKSAssertion _acquireAsynchronously] -> -[BKSProcessAssertion initWithBundleIdentifier:flags:reason:name:] : 120 -> 12
~ -[BKSAssertion _setAttributes:] -> -[BKSAssertion _lock_setAttributes:] : 84 -> 156
~ -[BKSAssertion _lock_setAttributes:] -> -[BKSAssertion _acquireAsynchronously] : 156 -> 120
~ -[BKSApplicationStateMonitor applicationInfoForPID:] -> -[BKSAssertion _setAttributes:] : 184 -> 84
~ _BKSProcessAssertionBackgroundTimeRemaining -> -[BKSApplicationStateMonitor applicationInfoForPID:] : 112 -> 184
~ -[BKSApplicationStateMonitor interestedStates] -> _BKSProcessAssertionBackgroundTimeRemaining : 56 -> 112
~ -[BKSAssertion setInvalidationHandler:] -> -[BKSApplicationStateMonitor interestedStates] : 104 -> 56
~ -[BKSProcessAssertion initWithBundleIdentifier:flags:reason:name:] -> -[BKSAssertion setInvalidationHandler:] : 12 -> 104

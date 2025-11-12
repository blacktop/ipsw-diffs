## AppSupportUI

> `/System/Library/PrivateFrameworks/AppSupportUI.framework/AppSupportUI`

```diff

 43.4.0.0.0
-  __TEXT.__text: 0x1ee50
+  __TEXT.__text: 0x1ee0c
   __TEXT.__auth_stubs: 0x420
   __TEXT.__objc_methlist: 0x182c
   __TEXT.__const: 0x181

   __TEXT.__unwind_info: 0x9a0
   __TEXT.__objc_classname: 0x2b2
   __TEXT.__objc_methname: 0x2eff
-  __TEXT.__objc_methtype: 0x1c11
+  __TEXT.__objc_methtype: 0x1c77
   __TEXT.__objc_stubs: 0x22c0
   __DATA_CONST.__got: 0x160
   __DATA_CONST.__const: 0x348

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A6F7CBE5-4431-3F38-8E62-30E30F8FF801
+  UUID: 15103990-A8B1-39EE-8B23-3C414A1BF4D2
   Functions: 704
   Symbols:   2365
   CStrings:  967
Functions:
~ -[NUIContainerGridView arrangedSubviewRows] : 244 -> 264
~ __ZNSt3__16vectorI23_NUIGridArrangementCellNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRP6UIViewR8_NSRangeSA_21NUIContainerAlignmentRSB_EEEPS1_DpOT_ : 396 -> 392
~ __ZNSt3__16vectorI23_NUIGridArrangementCellNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRP6UIViewR8_NSRangeSA_R21NUIContainerAlignmentSB_EEEPS1_DpOT_ : 396 -> 392
~ __ZN19_NUIFlowArrangement12measureCellsEb6CGSize : 1688 -> 1680
~ __ZNSt3__16vectorI23_NUIFlowArrangementCellNS_9allocatorIS1_EEE11__vallocateB8nn200100Em : 60 -> 64
~ __ZNSt3__16vectorI23_NUIGridArrangementCellNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJPU29objcproto18NUIArrangementItem11objc_object8_NSRangeS8_21NUIContainerAlignmentS9_EEEPS1_DpOT_ : 396 -> 392
~ __ZNSt3__16vectorI23_NUIGridArrangementCellNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJP28_NUIFlowArrangementDummyItem8_NSRangeS8_21NUIContainerAlignmentS9_EEEPS1_DpOT_ : 396 -> 392
~ __ZNSt3__16vectorI23_NUIGridArrangementCellNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKP20_NUIFlowRowContainer8_NSRangeSA_21NUIContainerAlignmentSB_EEEPS1_DpOT_ : 396 -> 392
~ __ZNSt3__16vectorI23_NUIGridArrangementCellNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRPU8__kindof6UIView8_NSRangeSA_21NUIContainerAlignmentSB_EEEPS1_DpOT_ : 396 -> 392
~ -[NUIContainerStackView populateGridArrangementDimension:withCells:axis:] : 2400 -> 2404
~ __ZNSt3__16vectorI23_NUIGridArrangementCellNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRPU29objcproto18NUIArrangementItem11objc_objectR8_NSRangeSA_R21NUIContainerAlignmentSC_EEEPS1_DpOT_ : 396 -> 392
~ -[UIView contentLayoutSizeCache] : 40 -> 36
~ -[UIView effectiveMinimumLayoutContentSize] : 188 -> 184
~ -[UIView effectiveMaximumLayoutContentSize] : 104 -> 100
~ -[_NUIFlowContainer initWithFlowArrangement:] : 64 -> 60
~ -[_NUIFlowContainer canUseSimpleGrid] : 84 -> 80
~ -[_NUIFlowRowContainer initWithFlowArrangement:cellRange:] : 76 -> 72
~ -[NUIContainerGridView _verticalAlignmentOfView:row:] : 128 -> 124
~ -[NUIGridDimension invalidateArrangedSubviews] : 52 -> 48
~ -[NUIGridDimension initWithContainerGridView:isRow:] : 136 -> 132
~ -[NUIContainerGridView _horizontalAlignmentOfView:inColumn:] : 120 -> 116
~ -[NUIContainerStackView _effectiveAlignmentForArrangedSubview:] : 84 -> 80
~ -[NUIBoxArrangement _cacheDisplayScaleIfNeeded] : 112 -> 108
~ -[NUIContainerFlowView _effectiveAlignmentForArrangedSubview:inAxis:] : 96 -> 92
~ -[NUIContainerBoxView _effectiveAlignmentForArrangedSubview:inAxis:] : 96 -> 92
~ -[NUIGridArrangement _cacheDisplayScaleIfNeeded] : 112 -> 108
CStrings:
+ "{_NUIBoxArrangement=\"container\"@\"<_NUIBoxArrangementContainer>\"\"horzDist\"q\"vertDist\"q\"hasValidMeasurement\"B\"cells\"{vector<_NUIBoxArrangementCell, std::allocator<_NUIBoxArrangementCell>>=\"__begin_\"^{_NUIBoxArrangementCell}\"__end_\"^{_NUIBoxArrangementCell}\"\"{?=\"__cap_\"^{_NUIBoxArrangementCell}}}\"measureSize\"{CGSize=\"width\"d\"height\"d}\"viewFrames\"{vector<CGRect, std::allocator<CGRect>>=\"__begin_\"^{CGRect}\"__end_\"^{CGRect}\"\"{?=\"__cap_\"^{CGRect}}}\"maxBaseLinePair\"{?=\"baseLineFromTop\"d\"baseLineFromBottom\"d}}"
+ "{_NUIFlowArrangement=\"container\"@\"<_NUIFlowArrangementContainer>\"\"horzDist\"b8\"vertDist\"b8\"baselineRelative\"B\"columns\"Q\"rowSpacing\"d\"itemSpacing\"d\"rowHeight\"d\"itemWidth\"d\"cells\"{vector<_NUIFlowArrangementCell, std::allocator<_NUIFlowArrangementCell>>=\"__begin_\"^{_NUIFlowArrangementCell}\"__end_\"^{_NUIFlowArrangementCell}\"\"{?=\"__cap_\"^{_NUIFlowArrangementCell}}}\"rows\"{vector<_NUIFlowRowContainer *, std::allocator<_NUIFlowRowContainer *>>=\"__begin_\"^@\"__end_\"^@\"\"{?=\"__cap_\"^@}}\"flowContainer\"@\"_NUIFlowContainer\"\"measuredWidth\"d\"viewFrames\"{vector<CGRect, std::allocator<CGRect>>=\"__begin_\"^{CGRect}\"__end_\"^{CGRect}\"\"{?=\"__cap_\"^{CGRect}}}\"maxBaseLinePair\"{?=\"baseLineFromTop\"d\"baseLineFromBottom\"d}}"
+ "{_NUIGridArrangement=\"container\"@\"<_NUIGridArrangementContainer>\"\"horzDist\"b8\"vertDist\"b8\"baselineRelative\"B\"hasValidMeasurement\"B\"cells\"{vector<_NUIGridArrangementCell, std::allocator<_NUIGridArrangementCell>>=\"__begin_\"^{_NUIGridArrangementCell}\"__end_\"^{_NUIGridArrangementCell}\"\"{?=\"__cap_\"^{_NUIGridArrangementCell}}}\"columns\"{vector<_NUIGridArrangementDimension, std::allocator<_NUIGridArrangementDimension>>=\"__begin_\"^{_NUIGridArrangementDimension}\"__end_\"^{_NUIGridArrangementDimension}\"\"{?=\"__cap_\"^{_NUIGridArrangementDimension}}}\"rows\"{vector<_NUIGridArrangementDimension, std::allocator<_NUIGridArrangementDimension>>=\"__begin_\"^{_NUIGridArrangementDimension}\"__end_\"^{_NUIGridArrangementDimension}\"\"{?=\"__cap_\"^{_NUIGridArrangementDimension}}}\"viewFrames\"{vector<CGRect, std::allocator<CGRect>>=\"__begin_\"^{CGRect}\"__end_\"^{CGRect}\"\"{?=\"__cap_\"^{CGRect}}}}"
+ "{map<UIView *, _NUIContainerViewArrangedSubview, std::less<UIView *>, std::allocator<std::pair<UIView *const, _NUIContainerViewArrangedSubview>>>=\"__tree_\"{__tree<std::__value_type<UIView *, _NUIContainerViewArrangedSubview>, std::__map_value_compare<UIView *, std::__value_type<UIView *, _NUIContainerViewArrangedSubview>, std::less<UIView *>>, std::allocator<std::__value_type<UIView *, _NUIContainerViewArrangedSubview>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{map<UIView *, const std::pair<_NSRange, _NSRange>, std::less<UIView *>, std::allocator<std::pair<UIView *const, const std::pair<_NSRange, _NSRange>>>>=\"__tree_\"{__tree<std::__value_type<UIView *, const std::pair<_NSRange, _NSRange>>, std::__map_value_compare<UIView *, std::__value_type<UIView *, const std::pair<_NSRange, _NSRange>>, std::less<UIView *>>, std::allocator<std::__value_type<UIView *, const std::pair<_NSRange, _NSRange>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{map<UIView *, double, std::less<UIView *>, std::allocator<std::pair<UIView *const, double>>>=\"__tree_\"{__tree<std::__value_type<UIView *, double>, std::__map_value_compare<UIView *, std::__value_type<UIView *, double>, std::less<UIView *>>, std::allocator<std::__value_type<UIView *, double>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{nui_size_cache=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}"
+ "{vector<CALayer *, std::allocator<CALayer *>>=\"__begin_\"^@\"__end_\"^@\"\"{?=\"__cap_\"^@}}"
- "{_NUIBoxArrangement=\"container\"@\"<_NUIBoxArrangementContainer>\"\"horzDist\"q\"vertDist\"q\"hasValidMeasurement\"B\"cells\"{vector<_NUIBoxArrangementCell, std::allocator<_NUIBoxArrangementCell>>=\"__begin_\"^{_NUIBoxArrangementCell}\"__end_\"^{_NUIBoxArrangementCell}\"__cap_\"^{_NUIBoxArrangementCell}}\"measureSize\"{CGSize=\"width\"d\"height\"d}\"viewFrames\"{vector<CGRect, std::allocator<CGRect>>=\"__begin_\"^{CGRect}\"__end_\"^{CGRect}\"__cap_\"^{CGRect}}\"maxBaseLinePair\"{?=\"baseLineFromTop\"d\"baseLineFromBottom\"d}}"
- "{_NUIFlowArrangement=\"container\"@\"<_NUIFlowArrangementContainer>\"\"horzDist\"b8\"vertDist\"b8\"baselineRelative\"B\"columns\"Q\"rowSpacing\"d\"itemSpacing\"d\"rowHeight\"d\"itemWidth\"d\"cells\"{vector<_NUIFlowArrangementCell, std::allocator<_NUIFlowArrangementCell>>=\"__begin_\"^{_NUIFlowArrangementCell}\"__end_\"^{_NUIFlowArrangementCell}\"__cap_\"^{_NUIFlowArrangementCell}}\"rows\"{vector<_NUIFlowRowContainer *, std::allocator<_NUIFlowRowContainer *>>=\"__begin_\"^@\"__end_\"^@\"__cap_\"^@}\"flowContainer\"@\"_NUIFlowContainer\"\"measuredWidth\"d\"viewFrames\"{vector<CGRect, std::allocator<CGRect>>=\"__begin_\"^{CGRect}\"__end_\"^{CGRect}\"__cap_\"^{CGRect}}\"maxBaseLinePair\"{?=\"baseLineFromTop\"d\"baseLineFromBottom\"d}}"
- "{_NUIGridArrangement=\"container\"@\"<_NUIGridArrangementContainer>\"\"horzDist\"b8\"vertDist\"b8\"baselineRelative\"B\"hasValidMeasurement\"B\"cells\"{vector<_NUIGridArrangementCell, std::allocator<_NUIGridArrangementCell>>=\"__begin_\"^{_NUIGridArrangementCell}\"__end_\"^{_NUIGridArrangementCell}\"__cap_\"^{_NUIGridArrangementCell}}\"columns\"{vector<_NUIGridArrangementDimension, std::allocator<_NUIGridArrangementDimension>>=\"__begin_\"^{_NUIGridArrangementDimension}\"__end_\"^{_NUIGridArrangementDimension}\"__cap_\"^{_NUIGridArrangementDimension}}\"rows\"{vector<_NUIGridArrangementDimension, std::allocator<_NUIGridArrangementDimension>>=\"__begin_\"^{_NUIGridArrangementDimension}\"__end_\"^{_NUIGridArrangementDimension}\"__cap_\"^{_NUIGridArrangementDimension}}\"viewFrames\"{vector<CGRect, std::allocator<CGRect>>=\"__begin_\"^{CGRect}\"__end_\"^{CGRect}\"__cap_\"^{CGRect}}}"
- "{map<UIView *, _NUIContainerViewArrangedSubview, std::less<UIView *>, std::allocator<std::pair<UIView *const, _NUIContainerViewArrangedSubview>>>=\"__tree_\"{__tree<std::__value_type<UIView *, _NUIContainerViewArrangedSubview>, std::__map_value_compare<UIView *, std::__value_type<UIView *, _NUIContainerViewArrangedSubview>, std::less<UIView *>>, std::allocator<std::__value_type<UIView *, _NUIContainerViewArrangedSubview>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
- "{map<UIView *, const std::pair<_NSRange, _NSRange>, std::less<UIView *>, std::allocator<std::pair<UIView *const, const std::pair<_NSRange, _NSRange>>>>=\"__tree_\"{__tree<std::__value_type<UIView *, const std::pair<_NSRange, _NSRange>>, std::__map_value_compare<UIView *, std::__value_type<UIView *, const std::pair<_NSRange, _NSRange>>, std::less<UIView *>>, std::allocator<std::__value_type<UIView *, const std::pair<_NSRange, _NSRange>>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
- "{map<UIView *, double, std::less<UIView *>, std::allocator<std::pair<UIView *const, double>>>=\"__tree_\"{__tree<std::__value_type<UIView *, double>, std::__map_value_compare<UIView *, std::__value_type<UIView *, double>, std::less<UIView *>>, std::allocator<std::__value_type<UIView *, double>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
- "{nui_size_cache=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"
- "{vector<CALayer *, std::allocator<CALayer *>>=\"__begin_\"^@\"__end_\"^@\"__cap_\"^@}"

```

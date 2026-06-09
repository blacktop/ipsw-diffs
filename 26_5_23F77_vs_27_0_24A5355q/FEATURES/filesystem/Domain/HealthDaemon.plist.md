## HealthDaemon.plist

> `Domain/HealthDaemon.plist`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>AllowExperimentalHealthTypesUsage</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>BatchedRouteSmoothingWatch</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>BloodPressureValidationsEnabled</key>
 	<dict>
 		<key>DevelopmentPhase</key>

 	</dict>
 	<key>CachedStatisticsCollectionQueries</key>
 	<dict>
-		<key>Enabled</key>
-		<true/>
-	</dict>
-	<key>CloudSyncSharding</key>
-	<dict>
-		<key>Enabled</key>
-		<true/>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
 	</dict>
 	<key>CoalesceCumulativeTypesInWorkoutSeries</key>
 	<dict>

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
-	<key>CondenseFirstPartyiOSWorkouts</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
 	<key>CondenseWorkoutSamplesFromNonWatchSources</key>
 	<dict>
 		<key>DevelopmentPhase</key>

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
-	<key>DatabasePruningTaskShouldUseRestrictionPredicates</key>
+	<key>DatabaseStatementCacheTransactionScoping</key>
 	<dict>
 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
-	<key>DatabaseStatementCacheTransactionScoping</key>
-	<dict>
-		<key>Enabled</key>
-		<true/>
-	</dict>
 	<key>DatabaseValueCacheTransactionScoping</key>
 	<dict>
-		<key>Enabled</key>
-		<true/>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
 	</dict>
 	<key>EvaluateSyncEntityVersionForTakeover</key>
 	<dict>
 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>HRPassiveSeriesAggregation</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>HRWorkoutSeriesAggregation</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>HeartRateCoordinator</key>
 	<dict>
 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>MaintenanceWorkThroughOrchestration</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>OrchestrationMCDataObservation</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>SingleTransactionApplySyncChange</key>
 	<dict>
 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>TrainingLoadCache</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>UnifiedCloudSync</key>
 	<dict>
 		<key>DevelopmentPhase</key>

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
-	<key>WorkoutSavingQueryPerf</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
 	<key>WorkoutSeriesAggregation</key>
 	<dict>
 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
-	<key>WorkoutTempTableChanges</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
 	<key>XPCGatedSecondaryJournalMergeForVisionPro</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

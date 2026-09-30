## HealthDaemon.plist

> `Domain/HealthDaemon.plist`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>AnalyticsSubmissionOnMaintenanceWorkCoordinator</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>CachedStatisticsCollectionQueries</key>
 	<dict>
 		<key>Enabled</key>

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>CoalesceCumulativeTypesInWorkoutSeries</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>CoalesceHeartRatesInWorkoutSeries</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>CondenseFirstPartyiOSWorkouts</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>CondenseWorkoutSamplesFromNonWatchSources</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>DatabasePrioritySemaphore</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>DatabasePruningTaskShouldUseRestrictionPredicates</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>DatabaseStatementCacheTransactionScoping</key>
 	<dict>
 		<key>Enabled</key>

 		<key>Enabled</key>
 		<true/>
 	</dict>
-	<key>StringCache</key>
+	<key>EvaluateSyncEntityVersionForTakeover</key>
 	<dict>
-		<key>Enabled</key>
-		<true/>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
 	</dict>
-	<key>WorkoutRouteSmoothing</key>
+	<key>HeartRateCoordinator</key>
 	<dict>
-		<key>Enabled</key>
-		<true/>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>SingleTransactionApplySyncChange</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>UnifiedCloudSync</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>WorkoutCondensationOnLocking</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>WorkoutMirroringBackgroundAssertion</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>WorkoutSeriesAggregation</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
 	</dict>
 	<key>XPCGatedSecondaryJournalMergeForVisionPro</key>
 	<dict>
 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>healthDataclassForNirha</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>sharedStoreXPC</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 </dict>
 </plist>
 

```

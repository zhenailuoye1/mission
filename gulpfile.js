var gulp = require("gulp");
var ts = require("gulp-typescript");
var tsProject = ts.createProject("tsconfig.json");
var sass = require('gulp-sass');

gulp.task("ts", function () {
    return tsProject.src("assets/ts/")
        .pipe(ts(tsProject))
        .js.pipe(gulp.dest("static/js/"));
});


gulp.task('scss', function() {
    gulp.src('./assets/scss/*.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('./static/css/'))
});

gulp.task('sass_watcher',function() {
    gulp.watch('sass/**/*.scss',['styles']);
});

package com.bp.tim10.bptakmicenje;
import retrofit2.*;
import retrofit2.http.*;
import java.util.List;

/**
 * Created by ajlas on 01.01.2018..
 */

public interface EtfCompetitionRestClient {
    @FormUrlEncoded
    @POST("/api/login")
    Call<LoginResponse> login(@Field("email") String email, @Field("password") String password);
    @GET("/api/search/competition")
    Call<List<CompetitionResponse>> getCompetitions();


}

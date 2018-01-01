package com.bp.tim10.bptakmicenje;


import android.content.Intent;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import android.widget.Toast;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

/**
 * A simple {@link Fragment} subclass.
 */
public class Takmicenja extends Fragment {


    public Takmicenja() {
        // Required empty public constructor
    }


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_takmicenja, container, false);
    }

    @Override
    public void onStart() {
        super.onStart();

        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://10.0.2.2:5000/")
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        EtfCompetitionRestClient service = retrofit.create(EtfCompetitionRestClient.class);
        Call<List<CompetitionResponse>> login = service.getCompetitions();
        login.enqueue(new Callback<List<CompetitionResponse>>() {
            @Override
            public void onResponse(Call<List<CompetitionResponse>> call, Response<List<CompetitionResponse>> response) {
                List<CompetitionResponse> listaTakmicenja = response.body();
                TakmicenjaArrayAdapter adapter = new TakmicenjaArrayAdapter(getActivity(), listaTakmicenja);
                ListView listView = (ListView)getView().findViewById(R.id.simpleListView);
                listView.setAdapter(adapter);
            }

            @Override
            public void onFailure(Call<List<CompetitionResponse>> call, Throwable t) {
                call.cancel();
                Toast.makeText(getActivity(), "Network error.", Toast.LENGTH_LONG).show();
            }

        });




    }



}
